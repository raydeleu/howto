import cadquery as cq

car_length      = 50;
car_width       = 20;
overhang_front  = 8;
overhang_rear   = 9;
cabin_width     = 16;
cabin_length    = 26; 
# 33 = station, 26=sedan, 15=pickup
car_height      = 14;
bonnet_height   = 8;
bonnet_rounding = 4;
bonnet_length   = 15;
wheel_radius    = 4.5;
tire_width      = 3;
tire_protrude   = 1;
rim_height      = 1;
tire_compression= 1;
road_clearance  = 3;
wheelSpacing    = 0.5;

# Derived properties
wheel_base      = car_length - overhang_front - overhang_rear;
cabin_narrowing = (car_width - cabin_width)/2;
cabin_base      = road_clearance + bonnet_height + 0.5*(car_height-bonnet_height)
cabin_height    = car_height-bonnet_height

# Draw car body and passenger cabin
car_body        = cq.Workplane("XY").box(car_length,car_width,bonnet_height)
car_body        = car_body.translate((0,0,bonnet_height/2 + road_clearance))

car_cabin       = cq.Workplane("XY").box(cabin_length, cabin_width, cabin_height)
car_cabin       = car_cabin.translate((cabin_length/2 - bonnet_length,0,cabin_base))
car_cabin       = car_cabin.edges("|Y and >Z").chamfer(cabin_height-0.1)
car_cabin       = car_cabin.edges("|Y and >Z").fillet(2)
car_cabin       = car_cabin.edges(">Z").fillet(1)

# Sculpt the car body more aerodynamically
car_body_rounded = car_body.edges("|Y and >Z").fillet(bonnet_rounding)

# Round all edges
car_body_rounded = car_body_rounded.edges("|Y and <Z").fillet(1.5)
car_body_rounded = car_body_rounded.edges(">Y or <Y").fillet(1.5)
# cabin_aero       = car_cabin.edges("|Y and >Z").chamfer(cabin_height-0.1)
# cabin_aero       = cabin_aero.edges(">Y or <Y").fillet(1.5)

carBodyComplete = car_body_rounded.union(car_cabin)


# // Define wheels and wheel wells (Front/Rear - Left/Right)
rim              = cq.Workplane("XZ").cylinder(tire_width,wheel_radius-rim_height)
rim = rim.translate((car_length/2-overhang_front,\
                     car_width/2+tire_width/2-tire_protrude,\
                    wheel_radius-tire_compression))
wheel            = cq.Workplane("XZ").cylinder(tire_width,wheel_radius)
wheel = wheel.translate((car_length/2-overhang_front,\
                     car_width/2-tire_width/2,\
                    wheel_radius-tire_compression))
wheelwell            = cq.Workplane("XZ").cylinder(tire_width,wheel_radius+wheelSpacing)
wheelwell = wheelwell.translate((car_length/2-overhang_front,\
                     car_width/2-tire_width/2,\
                    wheel_radius-tire_compression))    
    
wheelwellFL = wheelwell
wheelwellRL = wheelwell.translate((-wheel_base,0,0))
wheelwellFR = wheelwell.translate((0,-car_width+tire_width,0))
wheelwellRR = wheelwellFR.translate((-wheel_base,0,0))

carBodyComplete = carBodyComplete.cut(wheelwellFL)
carBodyComplete = carBodyComplete.cut(wheelwellRL)
carBodyComplete = carBodyComplete.cut(wheelwellFR)
carBodyComplete = carBodyComplete.cut(wheelwellRR)
    
wheelFL = wheel.cut(rim)
wheelRL = wheelFL.translate((-wheel_base,0,0))
wheelFR = wheelFL.mirror("XZ")
wheelRR = wheelFR.translate((-wheel_base,0,0))

show_object(carBodyComplete)
show_object(wheelFL)
show_object(wheelFR)
show_object(wheelRL)
show_object(wheelRR)
