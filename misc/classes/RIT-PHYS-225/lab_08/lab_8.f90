program Integral

    ! Variables
    real(8) :: a, b
    integer :: n
    
    ! Interval variables
    real(8) :: x
    real(8) :: y
    real(8) :: dx
    
    ! Sum variables
    real(8) :: left = 0.0
    real(8) :: right = 0.0
    real(8) :: middle = 0.0
    real(8) :: exact = 0.0
    
    ! Read input from console
    write(*, *) "Left bound: "
    read(*, *) a
    write(*, *) "Right bound: "
    read(*, *) b
    write(*, *) "Number of boxes: "
    read(*, *) n
    
    ! Calculate delta x
    dx = (b - a) / n
    
    
    ! Calculate left definite integral
    x = a
    do i = 1, n
        left = left + 5 * x ** 3 + 6 * x ** 2
        x = x + dx
    end do
    left = left * dx
    
    ! Calculate right definite integral
    x = a + dx
    do j = 1, n
        right = right + 5 * x ** 3 + 6 * x ** 2
        x = x + dx
    end do
    right = right * dx
        
    ! Calculate middle definite integral
    x = a + 0.5 * dx
    do k = 1, n
        middle = middle + 5 * x ** 3 + 6 * x ** 2
        x = x + dx
    end do
    middle = middle * dx
    
    ! Calculate exact definite integral
    exact = ( 1.25 * b ** 4 + 2 * b ** 3) - ( 1.25 * a ** 4 + 2 * a ** 3)


    ! Print results
    write(*, *) "Left-hand sum:  ", left,   "(Error:", dabs(left   - exact) / exact, ")" 
    write(*, *) "Right-hand sum: ", right,  "(Error:", dabs(right  - exact) / exact, ")"
    write(*, *) "Centerpoint sum:", middle, "(Error:", dabs(middle - exact) / exact, ")"
    write(*, *) "Exact integral: ", exact
    
end program Integral