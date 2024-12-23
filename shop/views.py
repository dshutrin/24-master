from django.contrib.humanize.templatetags.humanize import intcomma
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required

from random import choice

from .forms import *
from .models import *
from .utils import *


# Create your views here.
def home(request):

	class MainCats:
		def __init__(self, category):
			self.category = category
			cat = CatImage.objects.filter(category=category)
			if len(cat) > 0:
				cat = cat[0]
				self.image = cat.image.url
			else:
				self.image = ''

	cats_all = Category.objects.filter(show_on_home=True)
	cats = [MainCats(x) for x in cats_all[:3]]
	cats2 = [MainCats(x) for x in cats_all[3:5]]

	return render(request, 'new_ui/home.html', {
		'cats': cats,
		'cats2': cats2,
	})


def catalog(request):

	class Pinfo:
		def __init__(self, prod):
			self.prod = prod

			if request.user.is_authenticated:
				self.in_trash = len(UserTrash.objects.filter(user=request.user, product=self.prod)) > 0

				if self.in_trash:
					self.in_trash_count = UserTrash.objects.filter(user=request.user, product=self.prod).first().pcount

			else:
				self.in_trash = False

	all_cats = Category.objects.all()

	if request.method == 'GET':
		products = Product.objects.all()
		products = [Pinfo(x) for x in products]

		return render(request, 'new_ui/catalog.html', {
			'cats': all_cats,
			'products': products
		})

	elif request.method == 'POST':

		products = Product.objects.all()

		if request.POST['cat']:

			if request.POST['cat'].isdigit():
				products = [x.product for x in ProductCategory.objects.filter(category__id=int(request.POST['cat']))]

		if request.POST['code_ch']:
			products = [x for x in products if request.POST['code_ch'].lower() in x.product_code.lower()]

		if request.POST['n_ch']:
			products = [x for x in products if request.POST['n_ch'].lower() in x.name.lower()]

		if request.POST['a_s_ch']:
			if request.POST['a_s_ch'].isdigit():
				products = [x for x in products if x.age_start >= int(request.POST['a_s_ch'])]

		if request.POST['a_e_ch']:
			if request.POST['a_e_ch'].isdigit():
				products = [x for x in products if x.age_start <= int(request.POST['a_e_ch'])]

		if request.POST['h_s_ch']:
			if request.POST['h_s_ch'].isdigit():
				products = [x for x in products if x.height >= int(request.POST['h_s_ch'])]

		if request.POST['h_e_ch']:
			if request.POST['h_e_ch'].isdigit():
				products = [x for x in products if x.height <= int(request.POST['h_e_ch'])]

		if request.POST['w_s_ch']:
			if request.POST['w_s_ch'].isdigit():
				products = [x for x in products if x.width >= int(request.POST['w_s_ch'])]

		if request.POST['w_e_ch']:
			if request.POST['w_e_ch'].isdigit():
				products = [x for x in products if x.width <= int(request.POST['w_e_ch'])]

		if request.POST['l_s_ch']:
			if request.POST['l_s_ch'].isdigit():
				products = [x for x in products if x.length >= int(request.POST['l_s_ch'])]

		if request.POST['l_e_ch']:
			if request.POST['l_e_ch'].isdigit():
				products = [x for x in products if x.length <= int(request.POST['l_e_ch'])]

		if request.POST['price_s_ch']:
			if request.POST['price_s_ch'].isdigit():
				products = [x for x in products if x.price >= int(request.POST['price_s_ch'])]

		if request.POST['price_e_ch']:
			if request.POST['price_e_ch'].isdigit():
				products = [x for x in products if x.price <= int(request.POST['price_e_ch'])]

		products = [Pinfo(x) for x in products]

		return render(request, 'new_ui/catalog.html', {
			'cats': all_cats,
			'products': products
		})


@csrf_exempt
def update_uitp_count(request):
	if request.method == 'POST':

		uid = int(request.POST['uid'])
		pid = int(request.POST['pid'])
		val = int(request.POST['val'])

		trash = UserTrash.objects.get(user__id=uid, product__id=pid)
		trash.pcount = val
		trash.save()

		return JsonResponse({}, status=200)


@csrf_exempt
def update_uitp_count_(request):
	if request.method == 'POST':

		uid = int(request.POST['uid'])
		pid = int(request.POST['pid'])
		val = int(request.POST['val'])

		trash = UserTrash.objects.get(user__id=uid, product__id=pid)
		trash.pcount = val
		trash.save()

		sm = intcomma(str(sum([x.product.price * x.pcount for x in UserTrash.objects.filter(user__id=uid)]))).replace(',', ' ')

		return JsonResponse({
			'sm': sm
		}, status=200)


@login_required
@csrf_exempt
def remove_product_from_trash(request):
	if request.method == 'POST':

		pid = int(request.POST['pid'])
		UserTrash.objects.get(id=pid).delete()

		sm = intcomma(str(sum([x.product.price * x.pcount for x in UserTrash.objects.filter(user=request.user)]))).replace(
			',', ' ')

		return JsonResponse({
			'sm': sm
		}, status=200)



@csrf_exempt
def add_product_to_trash(request):
	if request.method == 'POST':

		try:
			prod = Product.objects.get(id=int(request.POST['pid']))

			UserTrash.objects.create(
				user=request.user,
				product=prod,
				pcount=1
			)

			return JsonResponse({}, status=200)

		except:
			return JsonResponse({}, status=500)


def about(request):
	return render(request, 'new_ui/about.html')


def trash(request):
	products = UserTrash.objects.filter(user=request.user)
	total_sum = sum([x.product.price * x.pcount for x in products])

	user_contacts = False
	if request.user.is_authenticated:
		if request.user.email:
			user_contacts = True
		if request.user.phone_number:
			user_contacts = True

	return render(request, 'new_ui/trash.html', {
		'user_contacts': user_contacts,
		'products': products,
		'pcount': len(products),
		'total_sum': total_sum
	})


@login_required
@csrf_exempt
def add_order(request):
	if request.method == 'POST':

		uid = int(request.POST['uid'])

		if uid == request.user.id:

			contacts = ''

			if request.user.email:
				contacts += f'email: {request.user.email} '
			if request.user.phone_number:
				contacts += f'Номер телефона: {request.user.phone_number} '

			is_good = True

			try:
				order = Order.objects.create(
					user=request.user,
					contacts=contacts,
					total_price=sum([x.product.price * x.pcount for x in UserTrash.objects.filter(user=request.user)])
				)

				for prod in UserTrash.objects.filter(user=request.user):
					OrderElement.objects.create(
						order=order,
						product=prod.product,
						pcount=prod.pcount,
						total_price=prod.product.price * prod.pcount,
					)
			except Exception as e:
				is_good = False
				return JsonResponse({}, status=500)

			if is_good:
				UserTrash.objects.filter(user=request.user).delete()
				return JsonResponse({}, status=200)

			return JsonResponse({}, status=500)

		else:
			return JsonResponse({}, status=500)


@login_required
def profile(request):

	orders = Order.objects.filter(user=request.user).order_by('-status', '-create_at')

	return render(request, 'new_ui/profile.html', {
		'orders': orders
	})


@login_required
@csrf_exempt
def update_contacts(request):
	if request.method == 'POST':

		try:
			email = request.POST['email']
			phone = int(request.POST['phone_number'])

			request.user.phone_number = phone
			request.user.email = email

			request.user.save()

			return JsonResponse({}, status=200)
		except:
			return JsonResponse({}, status=500)


@login_required
def detail_order(request, oid):
	order = Order.objects.get(id=oid)

	if order.user == request.user:

		items = OrderElement.objects.filter(order=order)
		ts = sum([x.total_price for x in items])
		tpcount = sum([x.pcount for x in items])

		return render(request, 'new_ui/order_detail.html', {
			'order': order,
			'items': items,
			'ts': ts,
			'tpcount': tpcount
		})

	else:
		return HttpResponse(status=404)


def login(request):
	if request.method == 'GET':
		return render(request, 'new_ui/login_page.html')
	elif request.method == 'POST':
		username = request.POST["username"]
		password = request.POST["password"]
		usr = authenticate(request, username=username, password=password)
		if usr is not None:
			user_login(request, usr)
			return HttpResponseRedirect('/')
		else:
			return render(request, 'new_ui/login_page.html')


def logout(request):
	user_logout(request)
	return HttpResponseRedirect('/')


def registration(request):
	if request.method == 'GET':
		return render(request, 'new_ui/reg.html', {
			'form': RegForm()
		})
	elif request.method == 'POST':
		form = RegForm(request.POST)
		if form.is_valid():

			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			psw1 = form.cleaned_data['password']
			psw2 = form.cleaned_data['password2']

			if psw1 == psw2:

				user = CustomUser.objects.create_user(username=username, email=email, password=psw1)
				user.set_password(psw1)
				user.save()

				user_login(request, user)
				return HttpResponseRedirect('/')

			else:
				return render(request, 'new_ui/reg.html', {
					'form': form
				})

		else:
			return render(request, 'new_ui/reg.html', {
				'form': form
			})

