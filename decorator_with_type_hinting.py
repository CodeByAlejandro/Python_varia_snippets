from typing import ( Any, Callable, Concatenate, Dict, ParamSpec, TypeVar, Union )

UserDict = Dict[str, Union[str, bool]]

user1: UserDict = {
    'name': 'Sorna',
    'valid': True
}

P = ParamSpec("P")
R = TypeVar("R")

FunctionWithUserArgsKwargs = Callable[Concatenate[UserDict, P], R]

def authenticated(fn: FunctionWithUserArgsKwargs) -> FunctionWithUserArgsKwargs:
    def wrapper_fn(user: UserDict, *args: Any, **kwargs: Any) -> Any:
        if user.get('valid', False):
            return fn(user, *args, **kwargs)
        else:
            print("User is not valid")
    return wrapper_fn

@authenticated
def message_friends(user: UserDict) -> None:
    print(f'message has been sent for user {user}')

message_friends(user1)
user1['valid'] = False
message_friends(user1)
user1['valid'] = True
message_friends(user1)
