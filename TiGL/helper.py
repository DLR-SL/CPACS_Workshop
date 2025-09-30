from OCC.Display.WebGl.jupyter_renderer import JupyterRenderer

def display(aircraft):
    """
    displays the fuselages and wings of a CPACS configuration
    using the JupyterRenderer of pythonocc
    """
    
    # create a list of shapes to display
    shapes = []
    for i in range(1, aircraft.get_wing_count()+1):
        wing = aircraft.get_wing(i)
        shapes.append(wing.get_loft().shape())
        mirrored_shape = wing = wing.get_mirrored_loft()
        if mirrored_shape is not None:
            shapes.append(mirrored_shape.shape())
    
    for i in range(1, aircraft.get_fuselage_count()+1):
        fuselage = aircraft.get_fuselage(i)
        shapes.append(fuselage.get_loft().shape())
    
    renderer = JupyterRenderer()
    
    for shape in shapes:
        renderer.DisplayShape(
            shape,
            render_edges=True,
            edge_color="black",
            topo_level="Face",
            update=False)
    
    renderer.Display()