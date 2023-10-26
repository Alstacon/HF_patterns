from chapter_11.person_classes import Person, OwnerProxy, NoOwnerProxy


def try_to_change_attr(obj, attr, args):
    try:
        getattr(obj, attr)(*args)
    except (AttributeError, PermissionError) as e:
        print(e)


def proxy_test_drive():
    bill_profile = Person('Bill', 'male', 'Java')
    bill_proxy = OwnerProxy(bill_profile)
    print(bill_proxy)
    print('''Bill is changing his name''')
    bill_proxy.set_name('Billboard')
    print(bill_proxy)
    print('''Bill is trying to change his rating''')
    try_to_change_attr(bill_proxy, 'set_geek_rating', (14,))

    bills_profile_visitor_proxy = NoOwnerProxy(bill_profile)
    print('''Someone's trying to change Bill's name''')
    bills_profile_visitor_proxy.set_name('Billy')
    print(bills_profile_visitor_proxy)
    print('''Someone changed Bill's rating''')
    try_to_change_attr(bills_profile_visitor_proxy, 'set_geek_rating', (100,))
    print(bills_profile_visitor_proxy)

    leslie = Person('Leslie', 'female', 'GO')
    leslie_no_owner_proxy = NoOwnerProxy(leslie)
    print(leslie_no_owner_proxy)
    print('''Someone is trying to change Leslie's gender ''')
    leslie_no_owner_proxy.set_gender('male')


if __name__ == '__main__':
    proxy_test_drive()
