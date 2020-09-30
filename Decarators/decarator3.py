

def month_name_decarator(param):
  def outer(func):
    def inner():
        print((func() + '  ' + param).upper())
    return inner
  return outer

@month_name_decarator('September')
def month():
    return "this month is"

month()