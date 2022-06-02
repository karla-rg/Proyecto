from antlr.codCo import codCo
from util.structure import *
from this import s
from util.exceptions import *
from util.structure import _allCles as clasSele
from antlr.coolListener import coolListener

symAr = ['+', '-', '*', '/']
symRe = ['=', '>', '>=']
herCam = {'Bool': inheritsbool, 'String': inheritsstring, 'SELF_TYPE': inheritsselftype}
nomClasCam = {'Int': badredefineint, 'obje1ct': redefinedobje1ct, 'SELF_TYPE': selftyperedeclared}

class liste(coolListener):

    def __init__(self):
        clasSele.cl()
        setClas() #Klas
        self.main = False
        self.cuCl = None #Klas
        self.cuF = None

    def insinc(self, ctx: codCo.sincEnv):
        if ctx.num():
            sincNomb = ctx.num().obT()
            if sincNomb == 'self':
                raise selfEx('Error')

        if ctx.obje1():
            obje1 = ctx.obje1()
            if not obje1.sinc():
                if obtTi(ctx.obje1(), self.cuCl, self.cuF) == None: #Klass
                    raise outofscope('Error')

        if ctx.obtHered(1):
            if ctx.obtHered(1).obT() in symAr:
                obj1 = obtTi(ctx.sinc(0).obje1(), self.cuCl, self.cuF) #Klass
                sobj2 = obtTi(ctx.sinc(1).obje1(), self.cuCl, self.cuF) #Klass
                if obj1 != 'Int' or sobj2 != 'Int':
                    raise badarith("Error")
            if ctx.obtHered(1).obT() in symRe:
                obj1 = obtTi(ctx.sinc(0).obje1(), self.cuCl, self.cuF) #Klass
                sobj2 = obtTi(ctx.sinc(1).obje1(), self.cuCl, self.cuF) #Klass
                if obj1 != sobj2:
                    raise badequalitytest("Error")

    def inFu(self, ctx: codCo.envFu):
        funnum = ctx.num().obT()
        tiFun = ctx.TYPE().obT()
        if funnum == 'self' or funnum == 'SELF_TYPE':
            raise anattributenamedself("Error")
        if tiFun == 'SELF_TYPE':
            if ctx.sinc().inher[0].obT() != 'self':
                raise selftypebadreturn("Error")
        elif tiFun not in clasSele:
            raise returntypenoexist("Error")
        indicadores = []
        if ctx.inds:
            for ind in ctx.inds:
                for num in indicadores:
                    test = num[0]
                    if ind.num().obT() == num[0]:
                        test = "doble"
                        raise dobl("doble")
                indicadores.append([ind.num().obT(), ind.TYPE().obT()])
            self.cuF = fun(tiFun, inds=indicadores)
        else:
            self.cuF = fun(tiFun)

        try:
            funare = self.cuCl.upfun(funnum)
            if funare:
                for ind in ctx.inds:
                    if funare.inds[ind.num().obT()] != ind.TYPE().obT():
                        raise overrnumingfun4("Overrnuming")
                if len(funare.inds) != len(ctx.inds):
                    raise signaturechange("Changing")
            else:
                pass
        except KeyError:
            pass
        self.cuCl.addfun(funnum, self.cuF)

    def inLlaFu(self, ctx: codCo.LlaFuEnv):
        test = self.cuF
        funNo = ctx.num().obT()
        synLl = ctx.upHerCtx.obtHered(0).obje1()
        if ctx.upHerCtx.obtHered(1).obT() == '':
            synLl = liste.fifo(synLl)
            otSyn = ctx.upHerCtx.TYPE()

            if(upCl(obtTi(synLl, self.cuCl, self.cuF)).conforms(otSyn.obT())):
                raise trickyatdispatch2("Error")

        try:
            self.cuCl.upfun(funNo)
        except KeyError:
            raise baddispatch('Error')

    def exitsinc(self, ctx: codCo.sincEnv):
        if ctx.allowdecl(0):
            self.cuCl.closeScope()

                def fifo(obje1):
                    test = obje1.sinc()
                    if obje1.sinc():
                        if obje1.sinc().obje1():
                            return liste.fifo(obje1.sinc().obje1())

                return obje1

    def inCls(self, ctx: codCo.envCl): #Klss
        nombreCl = ctx.TYPE(0).obT()
        if nombreCl in nomClasCam:
            raise nomClasCam[nombreCl]()
        if ctx.TYPE(1):
            herCl = ctx.TYPE(1).obT()
            if herCl in herCam:
                raise herCam[herCl]()
            self.cuCl = Cla( #KLass
                nombreCl, inherits=ctx.TYPE(1).obT())
        else:
            self.cuCl = Cla(nombreCl)
        if nombreCl == 'Main':
            self.main = True

   def inEx(self, ctx: codCo.ExEnv):
        ftnum = ctx.num().obT()
        if ftnum == 'self' or ftnum == 'SELF_TYPE':
            raise anattributenamedself("Error")

        if ctx.sinc():
            if ctx.sinc().obje1():
                obje1 = liste.fifo(ctx.sinc().obje1())
                if obtTi(obje1, self.cuCl, self.cuF) == None:
                    raise attrbadinit("Error")

        try:
            x = self.cuCl.lookupAttribute(ftnum) #Klass
            if x:
                raise attroverride("Erro")
        except KeyError:
            pass

        self.cuCl.addAttribute(ftnum, ctx.TYPE().obT()) #Klass

    def inPut(self, ctx: codCo.PutEnv):
        self.cuCl.openScope()
        allownum = ctx.num().obT()

        if allownum == 'self' or allownum == 'SELF_TYPE':
            raise allowself("Error")

        self.cuCl.addScopeVariable(allownum, ctx.TYPE().obT())

    def inStruc(self, ctx: codCo.StrucEnv):
        if ctx.TYPE().obT() == 'SELF_TYPE':
            raise selftypeparameterposition('Error')
        if ctx.num().obT() == 'self':
            raise selfinformalparameter('Error')

    def exitCla(self, ctx: codCo.envCl):
        if (not self.main):
            raise nomain()
        self.cuCl = None

    def inRecL(self, ctx: codCo.RecLEnv):
        tiz = obtTi(liste.fifo(ctx.sinc(0).obje1()), self.cuCl, self.cuF) #Klass
        if tiz != 'Bool':
            raise badwhilecond("While ")

    def inCase(self, ctx: codCo.CaseEnv):
        ClTi = {''}
        for i in ctx.follC():
            if i.TYPE().obT() in ClTi:
                raise casenumenticalbranch("Error")
            else:
                ClTi.add(i.TYPE().obT())