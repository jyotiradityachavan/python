class employee:
    def __init__(self):
        print('Employee created')
    def __del__(self):
        print('Distructor called employee deleted')
obj=employee()
del obj            
        