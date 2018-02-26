'''
Created on 2018年2月26日

@author: Li
'''

def test_var_args(f_args, *argv):
    print('first normal arg:', f_args)
    for arg in argv:
        print('another arg through *argv:', arg)

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print('{0} == {1}'.format(key, value))
        
def test_args_kwargs(arg1, arg2, arg3):
    print('arg1:', arg1)
    print('arg2:', arg2)
    print('arg3:', arg3)
                
test_var_args('yasoob', 'python', 'eggs', 'test')
greet_me(name='yasoob')
#use *args
args = ('two', 3, 5)
test_args_kwargs(*args)

#use **kwargs
kwargs = {'arg3':3, 'arg2':'two', 'arg1':5}
test_args_kwargs(**kwargs)
#同时使用时，顺序为some_func(fargs, *args, **kwargs)