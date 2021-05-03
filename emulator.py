# BALAE BPU EMULATOR #
#      Brainf*k      #
#      Assembly      #
#      Language      #
#      Advanced      #
#      Edition       #

#  For the BrainF*k  #
#   derivative tut   #
#       series       #

#    Three storage   #
#      devices:      #

#        Tape        #
#    Tape Pointer    #
#   ProgramCounter   #

def blankout(s): pass
def blankin(): return 0

def balae(c,o0=blankout,o1=blankout,o2=blankout,o3=blankout,o4=blankout,o5=blankout,o6=blankout,o7=blankout,o8=blankout,o9=blankout,oA=blankout,oB=blankout,oC=blankout,oD=blankout,oE=blankout,oF=blankout,i0=blankin,i1=blankin,i2=blankin,i3=blankin,i4=blankin,i5=blankin,i6=blankin,i7=blankin,i8=blankin,i9=blankin,iA=blankin,iB=blankin,iC=blankin,iD=blankin,iE=blankin,iF=blankin):
  cd=[((ord(i)&0b11100000)>>5,ord(i)&0b00011111) for i in list(c)]
  tape=[0 for i in range(256)]
  pt=0
  pc=0

  outs=[o0,o1,o2,o3,o4,o5,o6,o7,o8,o9,oA,oB,oC,oD,oE,oF]
  ins=[i0,i1,i2,i3,i4,i5,i6,i7,i8,i9,iA,iB,iC,iD,iE,iF]

  def arithmetic(a):
    nonlocal tape
    nonlocal pt
    nonlocal pc
    nonlocal cd

    mod=a-16

    tape[pt]=(tape[pt]+mod)%256

    return True
  def pointer(a):
    nonlocal tape
    nonlocal pt
    nonlocal pc
    nonlocal cd

    mod=a-16

    pt=(pt+mod)%256

    return True
  def ifzero(a):
    nonlocal tape
    nonlocal pt
    nonlocal pc
    nonlocal cd

    if tape[pt]==0:
      pc+=a
      return False
  def userinteract(a):
    nonlocal tape
    nonlocal pt
    nonlocal pc
    nonlocal cd
    nonlocal outs
    nonlocal ins

    if a<16:
      outs[a](tape[pt])
    else:
      tape[pt]=ins[a]()%256
    return True
  def jumpfore(a):
    nonlocal tape
    nonlocal pt
    nonlocal pc
    nonlocal cd

    while cd[pc][1]!=a or cd[pc][0]!=6:
      pc+=1
    return False
  def jumpback(a):
    nonlocal tape
    nonlocal pt
    nonlocal pc
    nonlocal cd

    while cd[pc][1]!=a or cd[pc][0]!=6:
      pc-=1
    return False
  def label(a):
    return True

  coms=[arithmetic,pointer,ifzero,userinteract,jumpfore,jumpback,label]

  while True:
    if cd[pc][0]==7:
      break
    else:
      if coms[cd[pc][0]](cd[pc][1]):
        pc+=1
