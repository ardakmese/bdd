from behave import given, when, then
from calculator import subtract

@given(u'Calculator app is run for subtraction')
def step_impl(context):
    print(u'Step: Given Calculator app is run')

@when(u'I subtract "{a}" and "{b}" using calculator')
def step_impl(context, a, b):
    print(u'Step: When I subtract "{}" and "{}" using calculator'. format(a, b))
    context.result = subtract(a, b)
    print(u'Stored result "{}" in context'. format(context.result))

@then(u'I get from subtraction "{out}"')
def step_impl(context, out):
    if (context.result == int(out)):
        print(u'Step: Then I get right result "{}", "{}"'.format(context.result, out))
        pass
    else:
        raise Exception("Invalid subtraction is returned.")
