number = "51621232927393794428283281722302417684416215565352081372219649050894399902811978842493025898332777796978839725641"

found = False
f1 = 1
f2 = 1

def top_digits(n):
  t = n * 0.20898764024997873 + (-0.3494850021680094)
  t = int((pow(10, t - int(t) + 8)))
  return t

def istoppandigital(n):
    if range(1,10) == top_digits(n):
        return True

def ispandigital(n):
    n = str(n)
    first_pandigital = top_digits(int(n))
    last_pandigital = n[-9:]
    list_last_pandigital = list(last_pandigital)
    list_first_pandigital = list(first_pandigital)
    list_last_pandigital.sort()
    list_first_pandigital.sort()
    if  ['1','2','3','4','5','6','7','8','9'] == list_last_pandigital and ['1','2','3','4','5','6','7','8','9'] == list_first_pandigital:
            return True
    else:
            return False

counter = 2
while not found:
    fn = f1 + f2
    f2 = f1
    f1 = fn
    counter = counter + 1
    print "%s" % (counter)
    # if str(fn) == number:
    #     print "S"
    #     import pdb;pdb.set_trace()
    if counter == 541:
        import pdb; pdb.set_trace()
    if len(str(fn)) > 18:        
        if istoppandigital(fn):
            print "Fin no %s, %s, %s " % (counter, fn, len(str(fn)))

