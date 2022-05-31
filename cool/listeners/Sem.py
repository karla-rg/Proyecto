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

   
