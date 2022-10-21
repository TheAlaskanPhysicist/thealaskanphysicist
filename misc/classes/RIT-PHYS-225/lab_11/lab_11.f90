program RootFinder
    real(8) :: a = 0
    real(8) :: b = 5
    real(8) :: delta = 1e-4
    real(8) :: x
    real(8) :: f

    do while(dabs(b-a).ge.delta)
        x = (a + b) / 2
        f = 3 * x ** 2 - 5 * dexp(-x)
        if (f.lt.0) then
            a = x
        else
            b = x
        end if
    end do
    
    write(*, *) "x = ", x

end program RootFinder