import cadquery as cq

sketch = (
    cq.Sketch()
    .segment((0.,0),(0.,2.))
    .segment((2.,0))
    .close()
    .arc((.6,.6),0.4,0.,360.)
    .assemble(tag='face')
    .edges('%LINE',tag='face')
    .vertices()
    .chamfer(0.2)
    )

show_object(sketch)

result = (
   cq.Workplane("XY").placeSketch(sketch).extrude(0.1))

show_object(result)

# result2=(
#     cq.Workplane("ZX").placeSketch(sketch).extrude(0.1))

# result3=(
#     cq.Workplane("YZ").placeSketch(sketch).extrude(0.1))

# Workplane.all();

# result4 = cq.Workplane("XY").union(Workplane.all)