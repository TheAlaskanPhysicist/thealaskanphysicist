! Projectile Motion: ma + bv^2 + mg = 0
program AirResistanceProjectileMotion

    ! UNITS: SI
    real(8) :: PI = 3.1415926535
    real(8) :: g  = 9.81  ! Gravity (m/s²)
    
    ! State (Bozo) variables
    real(8) :: m  = 75.0  ! The mass of Bozo (kg)
    real(8) :: A  = 0.75  ! The cross-area of Bozo (m²)
    real(8) :: b   ! Coefficient of air resistance ( N/(m/s)² )
    real(8) :: bm  ! Ratio between b and m
    
    ! User input variables
    real(8) :: v      ! Speed |v| (m/s)
    real(8) :: theta  ! The angle of launch (rad)
    real(8) :: dt     ! Time interval length (s)

    ! State variables
    real(8) :: t  = 0.d0  ! Time (s)
    real(8) :: rx = 0.d0  ! X-position (m)
    real(8) :: ry = 0.d0  ! Y-position (m)
    real(8) :: vx = 0.d0  ! X-velocity (m/s)
    real(8) :: vy = 0.d0  ! Y-velocity (m/s)
    real(8) :: ax = 0.d0  ! X-acceleration (m/s²)
    real(8) :: ay = 0.d0  ! Y-acceleration (m/s²)
    real(8) :: maxrange


    ! Take in console input
    write(*, *) "Initial Velocity (m/s): "
    read(*, *) v
    write(*, *) "Initial Angle of Launch (degrees): "
    read(*, *) theta
    write(*, *) "Time-Step Interval (s): "
    read(*, *) dt


    ! Calculate the range equation for b = 0
    theta = theta * (PI / 180.0)
    maxrange = (v ** 2) * dsin(2 * theta) / g


    ! Initialize simulation
    ! b = 0.5 * A
    bm = b / m
    vx = v * dcos(theta)
    vy = v * dsin(theta)


    ! Run simulation
    do while( ry >= 0.0 )

        ! Find the speed
        v = dsqrt(vx ** 2 + vy ** 2)
        
        ! Calculate acceleration
        ax = -bm * v * vx
        ay = -bm * v * vy - g

        ! Iterate velocity
        vx = vx + ax * dt
        vy = vy + ay * dt

        ! Iterate position
        rx = rx + vx * dt
        ry = ry + vy * dt
        
        ! Add to total time
        t = t + dt
    
    end do


    ! Print results
    write(*, *) "Horizontal Displacement ", rx, "(meters)"
    write(*, *) "Projectile Time Duration", t, "(s)"
    write(*, *) "Range Equation Expected ", maxrange, "(meters)"
    
end program AirResistanceProjectileMotion