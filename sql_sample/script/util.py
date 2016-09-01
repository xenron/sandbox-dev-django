
def get_all_field(model):
    for field_name in model._meta.get_all_field_names():
        value = getattr(model, field_name, None)
        yield (field_name, value)

def print_all_field(model):
    print(dict(get_all_field(model)))