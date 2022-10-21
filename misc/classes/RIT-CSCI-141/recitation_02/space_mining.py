"""
CSCI-141 Computer Science 1 Recitation Exercise
02-VarsCondsFunctions
Space Mining

NASA is conducting space travel in order to gather three rare earth elements
from other nearby planets and the moon using various mining tools that
affect the yield of each mineral on each planet differently based on amounts.
"""

MARS_BONUS = 3
MERCURY_BONUS = 5
MOON_BONUS = 2
VENUS_BONUS = 4

def display_elements(planet, cerium, yttrium, scandium, space_rocks):
    """
    Display the elements gathered from a particular planet.
    :param planet: the planet name
    :param cerium: amount of cerium
    :param yttrium: amount of yttrium
    :param scandium: amount of scandium
    :param space_rocks: amount of space rocks
    """
    print(planet, 'yielded',
          cerium, 'cerium,',
          yttrium, 'yttrium',
          scandium, 'scandium and',
          space_rocks, 'space rocks')

def visit_mercury(drills):
    """
    Visit mercury and gather cerium.
    :param drills: number of drills sent
    :return: total amount of cerium gathered
    """
    if drills > 10:
        cerium = drills + 5 + MERCURY_BONUS
    else:
        cerium = drills + 2 + MERCURY_BONUS

    display_elements("Mercury", cerium, 0, 0, 0)

    return cerium

def visit_venus(drills, shovels):
    """
    Visit venus and gather yttrium.
    :param drills: number drills sent
    :param shovels: number of shovels sent
    :return: total amount of yttrium gathered
    """
    if shovels <= 6:
        yttrium = drills * 5 + shovels + VENUS_BONUS
    else:
        yttrium = (shovels + 1) // (drills // 2) + VENUS_BONUS

    display_elements("Venus", 0, yttrium, 0, 0)

    return yttrium

def visit_mars(drills, dozers):
    """
    Visit mars and gather scandium.
    :param drills: number of drills sent
    :param dozers: number of dozers sent
    :return: total amount of scandium gathered
    """
    if drills + dozers < 5:
        scandium = (drills + dozers) // 2 + MARS_BONUS
    elif drills + dozers >= 5 and drills + dozers < 20:
        scandium = drills * 3 // dozers + MARS_BONUS
    else:
        scandium = drills * 2 + 3 * dozers + MARS_BONUS

    display_elements("Mars", 0, 0, scandium, 0)

    return scandium

def visit_from_moon(drills, shovels, dozers):
    """
    Visit the moon and gather space rocks.

    :param drills: number of drills sent
    :param shovels: number of shovels sent
    :param dozers: number of dozers sent
    :return: total amount of space rocks gathered
    """
    _space_rock = 0

    # visit mercury.  the amount of space rocks obtained
    # from the cerium is multiplied by 2 plus the
    # global MOON_BONUS
    _cerium = visit_mercury(drills)
    _space_rock += 2 * _cerium + MOON_BONUS


    # visit venus.  the amount of space rocks obtained
    # is the amount of yttrium plus 3 plus the MOON_BONUS
    _yttrium = visit_venus(drills, shovels)
    _space_rock += _yttrium + 3 + MOON_BONUS


    # visit mars.  the amount of space rocks obtained
    # is integer divided by 2 plus the MOON_BONUS
    _scandium = visit_mars(drills, dozers)
    _space_rock += _scandium // 2 + MOON_BONUS


    # display the total yield from the moon
    display_elements("Moon", _cerium, _yttrium, _scandium, _space_rock)


    # return the total space rocks
    return _space_rock

def visit_from_earth():
    """
    Visit earth and see how many elements are gathered by several
    mining missions.
    """

    # first pay individual visits to each other planet
    cerium = visit_mercury(4)
    yttrium = visit_venus(2, 6)
    scandium = visit_mars(5, 3)

    # now visit the moon and gather the space rocks.  there are 10 drills,
    # 14 shovels and 11 dozers
    space_rock = visit_from_moon(10, 14, 11)

    # display the yield from the earth
    display_elements("Earth", cerium, yttrium, scandium, space_rock)

if __name__ == '__main__':
    visit_from_earth()
