from topaz.module import ClassDef
from topaz.objects.objectobject import W_Object
from topaz.coerce import Coerce

class W_DynamicLibraryObject(W_Object):
    classdef = ClassDef('DynamicLibrary', W_Object.classdef, filepath=__file__)

    @classdef.setup_class
    def setup_class(cls, space, w_cls):
        space.set_const(w_cls, "RTLD_LAZY", space.newint(1))
        space.set_const(w_cls, "RTLD_NOW", space.newint(2))
        space.set_const(w_cls, "RTLD_GLOBAL", space.newint(257))
        space.set_const(w_cls, "RTLD_LOCAL", space.newint(0))
        space.set_const(w_cls, 'Symbol', space.getclassfor(W_DL_SymbolObject))

    @classdef.singleton_method('allocate')
    def singleton_method_allocate(self, space, args_w):
        return W_DynamicLibraryObject(space)

    @classdef.singleton_method('open', flags='int')
    def method_open(self, space, w_name, flags):
        if w_name == space.w_nil:
            name = None
        else:
            name = Coerce.path(space, w_name)
        return W_DynamicLibraryObject(space)

    @classdef.method('find_variable', name='symbol')
    def method_find_variable(self, space, name):
        w_sym = space.find_const(self.getclass(space), 'Symbol')
        # TODO: return an instance of the class w_sym instead of just w_sym
        return w_sym.method_new(space, [], None)

class W_DL_SymbolObject(W_Object):
    classdef = ClassDef('Symbol', W_Object.classdef, filepath=__file__)

    @classdef.singleton_method('allocate')
    def singleton_method_allocate(self, space, args_w):
        return W_DL_SymbolObject(space)

    @classdef.method('null?')
    def method_null_p(self, space):
        return space.newbool(True)

    #@classdef.method('initialize')
    #def method_initialize(self, space):
    #    return W_DL_SymbolObject(space)
