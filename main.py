import time

#This is a binary counter coded by Roostersox!#
#Let's explain how this works.#
#These are the counter digits#
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
#Counter digits end here#

#Starting with while true, this makes an infinite loop.#
while True :
  print('abcdefgh')
  print(f'{a}{b}{c}{d}{e}{f}{g}{h}')
  time.sleep(1)
#This time delay is crucial to not exploding your cpu!#
#Ironically, CPUs hate doing their sole purpose - math.#
  h += 1
#Add one to the counter digit h#
  if h == 2:
      h = 0
      g += 1
#If h is equal to 2, then make it zero again,#
#and increment g by one.#
      if g == 2:
            g = 0
            f += 1
#Do the same thing with the other variables.#
            if f == 2:
                f = 0
                e += 1
#... ad nauseum.#
                if e == 2:
                    e = 0
                    d += 1
#... and again.#
                    if d == 2:
                        d = 0
                        c += 1
#... and again.#
                        if c == 2:
                            c = 0
                            b += 1
#You get the point, joke's not funny anymore, anyway.#
                            if b == 2:
                                b = 0
                                a += 1
#Ein mer.#
                                if a == 2:
                                    a = 0
#Cool thing is, this can be expanded infinitely. Just add another variable! Try it!#
#And that's it! Hope this helps a bit, in both Python and binary.#