Tests = [("z", "z", True),
         ("z", "y", False),
         ("z.z", "zz", True),
         ("z.z", "yz", False),
         ("z|y", "z", True),
         ("z|y", "y", True),
         ("z|y", "w", False),
         ("z.z|y", "zz", True),
         ("z.z|y", "y", True),
         ("z.z|y", "z", False),
         ("e*", "", True),
         ("e*", "eeeeee", True),
         ("e*", "eeezeee", False),
         ("z?", "z", True),
         ("z?", "", True),
         ("z?", "y", False),
         ("z|y.x?", "", False),
         ("z|y.x?", "y", True),
         ("z|y.x?", "yx", True),
         ("z|y.x?", "z", True)]
