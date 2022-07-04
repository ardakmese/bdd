from behave import given, when, then
from calculator import divide

@given(u'Calculator app is run for dividing')
def step_impl(context):
    print(u'Step: Given Calculator app is run')

@when(u'I divide "{a}" and "{b}" using calculator')
def step_impl(context, a, b):
    print(u'Step: When I divide "{}" and "{}" using calculator'. format(a, b))
    context.result = divide(a, b)
    print(u'Stored result "{}" in context'. format(context.result))

@then(u'I get from dividing "{out}"')
def step_impl(context, out):
    if (context.result == int(out)):
        print(u'Step: Then I get right result "{}", "{}"'.format(context.result, out))
        pass
    else:
        raise Exception("Invalid dividing is returned.")
