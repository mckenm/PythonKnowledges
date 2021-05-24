# How to reload or update developing module
While developing a python I always runing python with interactive mode, I keep ran into issue to reload a developing module when code get updated.   I previous need to exit python then rerun and import the module again, but that not effective, I later learn a better way by using reload(ModuleName)



```Python
import test
import test as t


reload(test)
reload(t)

```
