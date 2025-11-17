#Django Modules
from django.db.models import Q, Count, Avg, Max, Min, Sum, Case, When, F, Value, CharField, Model
from django.db.models.functions import ExtractYear, Now
from accounts.models import CustomUser
from django.utils.timezone import now, timedelta



# 2.1
q1 = CustomUser.objects.filter(is_active=True)

# 2.2
q2= CustomUser.objects.filter(email_endwith = "@gmail.com")

# 2.3
q3 = CustomUser.objects.filter(city = "Almaty")

# 2.4
q4 = CustomUser.object.exclude(city = "Almaty")

# 2.5
q5 = CustomUser.objects.filter(salary__gt=500000)

# 2.6
q6 = CustomUser.objects.filter(department = "IT", country = "Kazakhstan")

# 2.7
q7 = CustomUser.objects.filter(birth_date__isnull=True)

# 2.8
q8 = CustomUser.objects.filter(first_name__startswith='A')

# 2.9
q9 = CustomUser.objects.count()

# 2.10
q10 = CustomUser.objects.order_by('-date_joined')[:20]

# 2.11
q11 = CustomUser.objects.values_list("city", flat=True).distinct()

# 2.12
q12 = CustomUser.objects.filter(department = "Sales").count()

# 2.13
q13 = CustomUser.objects.filter(last_login__gte=now()-timedelta(days=7))

# 2.14
q14 = CustomUser.objects.annotate(Q(first_name__icontains='bek') | Q(last_name__icontains='bek'))

# 2.15
q15 = CustomUser.objects.filter(salary__range=(300000, 700000))

# 2.16
q16 = CustomUser.objects.filter(department__in=['HR', 'Finance','IT'])

# 2.17
q17 = CustomUser.objects.values("department").annotate(total_users=Count('id'))

# 2.18
q18 = q17.order_by('-total')

# 2.19
q19 = CustomUser.objects.values("city").annotate(total= Count('id')).order_by('-total')[:5] 

# 2.20
q20 = CustomUser.objects.filter(last_login__isnull=True)

# 2.21
q21 = CustomUser.objects.aggregate(avg_salary=Avg('salary'))

# 2.22
q22 = CustomUser.objects.aggregate(max_salary=Max('salary'), min_salary=Min('salary'))

# 2.23
q23 = CustomUser.objects.filter(phone__contains='+7')

# 2.24
q24 = CustomUser.objects.annotate(full_name=F('first_name') + Value(' ') + 'last_name')

# 2.25
q25 = CustomUser.objects.annotate(birth_year=ExtractYear('birth_date').order_by('birth_year'))

# 2.26
q26 = CustomUser.objects.filter(birth_date__mouth=5)

# 2.27
q27 = CustomUser.objects.filter(role = 'manager', salary__gt=400000)

# 2.28
q28 = CustomUser.objects.filter(Q(role= "employee") | Q(department = "HR")) 

# 2.29
q29 = CustomUser.objects.filter(is_active = True).values("city").annotate(total= Count('id'))

# 2.30
q30 = CustomUser.objects.order_by('-date_joined')[:10]

# 2.31
q31 = CustomUser.objects.filter(city__startswith='A', salary__gt=300000)

# 2.32
q32 = CustomUser.objects.filter(Q(department_isnull=True) | Q(department=""))

# 2.33
q33 = CustomUser.objects.values("country").annotate(
    total = Count('id'),
    avg_salary = Avg('salary')
)

# 2.34
q34 = CustomUser.objects.filter(is_staff=True).order_by('last_login')

# 2.35
q35 = CustomUser.objects.exclude(email_countains='example.com')

# 2.36
avg_sal = CustomUser.objects.aggregate(avg_salary=Avg('salary'))['avg_salary']
q36 = CustomUser.objects.filter(salary__gt=avg_sal)

# 2.37
q37 = CustomUser.objects.values("email").annotate(count = Count("id")).filter(count__gt=1)

# 2.38
q38 = CustomUser.objects.annotate(
    salary_level = Case(
        When(salary__lt=300000, then=Value('Low')),
        When(salary__gte=300000, salary__lte=700000, then=Value('Medium')),
        When(salary__gt=700000, then=Value('High')),
        output_field=CharField(),
    )
).order_by('salary_level')

# 2.39
q39 = CustomUser.objects.filter(date_joined__year=now().year)

# 2.40
q40 = CustomUser.objects.values("department").annotate(total_salary=Sum('salary'))

# 2.41
q41 = CustomUser.objects.filter(department="IT", last_login__isnull=True)

# 2.42
q42 = CustomUser.objects.filter(country="Kazakhstan").filter(Q(city_isnull=True) | Q(city=""))

# 2.43
q43 = CustomUser.objects.filter(birth_date__lt= "1990-01-01", salary__isnull=False)

# 2.44
q44 = CustomUser.objects.annotate(
    years_since_joined = (Now() - F('date_joined'))
)

# 2.45
q45 = CustomUser.objects.filter(
    department="Sales",
    email__endswith="@gmail.com",
    salary__gt=350000
)

# 2.46
q46 = CustomUser.objects.order_by("country", "salary")

# 2.47
q47 = CustomUser.objects.values("role").annotate(total=Count('id')).filter(total__gt=100)

# 2.48
q48 = CustomUser.objects.filter(last_login__lt=F("date_joined"))

# 2.49
q49 = CustomUser.objects.filter(
    is_senior = Case(
        When(birth_date__lte="1980-01-01", then=Value(True)),
        default=Value(False),
        output_field=Model.BooleanField(),
    )
)

# 2.50
q50 = CustomUser.objects.values("department").annotate(
    avg_salary = Avg('salary'),
    count = Count('id')
).filter(count__gte=20).order_by('-avg_salary')




