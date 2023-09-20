# from NULL_not_found import NULL_not_found


# try:
#     Nothing = 123
#     Garlic = float(123)
#     Zero = 123
#     Empty = '123'
#     Fake = True
#     NULL_not_found(Nothing)
#     NULL_not_found(Garlic)
#     NULL_not_found(Zero)
#     NULL_not_found(Empty)
#     NULL_not_found(Fake)
#     print(NULL_not_found("Brian"))

# except Exception as e:
#     print(f"Exception: {e}")


from NULL_not_found import NULL_not_found


try:
    Nothing = None
    print(type(Nothing))
    Garlic = float("NaN")
    Zero = 0
    Empty = ''
    Fake = False
    NULL_not_found(Nothing)
    NULL_not_found(Garlic)
    NULL_not_found(Zero)
    NULL_not_found(Empty)
    NULL_not_found(Fake)
    print(NULL_not_found("Brian"))

except Exception as e:
    print(f"Exception: {e}")
