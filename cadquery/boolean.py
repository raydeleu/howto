import cadquery as cq

sphere = cq.Workplane("XY").sphere(8)
box    = cq.Workplane("YX").box(20,20,10)
box2 = box
box3 = box

box = box.cut(sphere)
box = box.edges("|Z").fillet(2)
box = box.edges(">X" or ">Y").fillet(1)


box2 = box2.cut(sphere)\
    .edges("|Z").fillet(2)\
    .edges(">X").fillet(1)\
    .edges(">Z").chamfer(0.5)\
    .translate((40,0,0))\

box3 = box3.intersect(sphere)\
      .edges(">Z").fillet(2)\
      .edges("<Z").chamfer(5)\
      .translate((0,40,0))\

show_object(box)
show_object(box2, options={"alpha":0.5, "color": (64, 164, 223)},name="test" )
show_object(box3, name = "intersect")
# show_object(sphere)

