from pyomexmeta import RDF, eUriType
cellml = """
<model xmlns="http://www.cellml.org/cellml/1.1#" xmlns:cmeta="http://www.cellml.org/metadata/1.0#" name="annotation_examples" cmeta:id="annExamples">
    <component name="membrane">
        <variable cmeta:id="membrane.V" name="V" public_interface="out" units="millivolt" />
    </component>

</model>
"""

rdf_graph_3_2_1 = RDF()
rdf_graph_3_2_1.set_archive_uri("physical_process.omex")
rdf_graph_3_2_1.set_model_uri("model.cellml")
annot_editor = rdf_graph_3_2_1.to_editor(cellml, generate_new_metaids=False, sbml_semantic_extraction=False)

#Sodium Channel
# with annot_editor.new_physical_entity() as sodium:
#     sodium \
#         .about("sodium", eUriType.LOCAL_URI) \
#         .identity("ChEBI:29101") \

with annot_editor.new_physical_entity() as sodium_channel_m_gate:
    sodium_channel_m_gate.about("local-entity-0", eUriType.LOCAL_URI) \
           .has_property("sodium_channel_m_gate.V", eUriType.MODEL_URI, "opb:OPB_00411")

with annot_editor.new_physical_entity() as sodium_channel_h_gate:
    sodium_channel_h_gate.about("local-entity-0", eUriType.LOCAL_URI) \
           .has_property("sodium_channel_h_gate.V", eUriType.MODEL_URI, "opb:OPB_00411")

# intracellular (FMA:66836) is portion of cytosol 
with annot_editor.new_physical_entity() as intracellular:
    intracellular \
        .about("intracellular", eUriType.LOCAL_URI) \
        .identity("FMA:66836")

with annot_editor.new_physical_entity() as extracellular:
    extracellular \
        .about("extracellular", eUriType.LOCAL_URI) \
        .identity("FMA:70022")
      
# Sodium channel activity (GO:0005272)
with annot_editor.new_physical_entity() as mediator_sodium_channel:
    mediator_sodium_channel \
        .about("mediator_sodium_channel", eUriType.LOCAL_URI) \
        .identity("GO:0005272") \

# Sodium Ions
with annot_editor.new_physical_entity() as sink_sodium:
    sink_sodium \
        .about("sink_sodium", eUriType.LOCAL_URI) \
        .identity("ChEBI:29101") \
        .is_part_of("intracellular", eUriType.LOCAL_URI)

# Sodium Ions
with annot_editor.new_physical_entity() as source_sodium:
    source_sodium \
        .about("source_sodium", eUriType.LOCAL_URI) \
        .identity("ChEBI:29101") \
        .is_part_of("extracellular", eUriType.LOCAL_URI)

with annot_editor.new_physical_process() as charge_flowrate_sodium:
    charge_flowrate_sodium \
        .about("process_sodium", eUriType.LOCAL_URI) \
        .add_source("source_sodium", eUriType.LOCAL_URI, multiplier=1) \
        .add_sink("sink_sodium", eUriType.LOCAL_URI, multiplier=1) \
        .add_mediator("mediator_sodium_channel", eUriType.LOCAL_URI) \
        .has_property(property_about="membrane.i_Na", about_uri_type=eUriType.MODEL_URI, is_version_of="opb:OPB_00318")

# ---------------------------------------------------------
#Potassium Channel Process
# with annot_editor.new_physical_entity() as potassium:
#     potassium \
#         .about("potassium", eUriType.LOCAL_URI) \
#         .identity("ChEBI:29103") \
    
# # plasma membrane (FMA:63841) is part of the cell (FMA:86454)
# with annot_editor.new_physical_entity() as plasma_membrane:
#     plasma_membrane \
#         .about("plasma_membrane", eUriType.LOCAL_URI) \
#         .identity("FMA:63841") \
#         .is_part_of("FMA:86454")

with annot_editor.new_physical_entity() as potassium_channel_n_gate:
    potassium_channel_n_gate.about("local-entity-0", eUriType.LOCAL_URI) \
           .has_property("potassium_channel_n_gate.V", eUriType.MODEL_URI, "opb:OPB_00411")

# Potassium channel activity (GO:0005267)
with annot_editor.new_physical_entity() as mediator_potassium_channel:
    mediator_potassium_channel \
        .about("mediator_potassium_channel", eUriType.LOCAL_URI) \
        .identity("GO:0005267")

# Potassium Ions
with annot_editor.new_physical_entity() as source_potassium:
    source_potassium \
        .about("source_potassium", eUriType.LOCAL_URI) \
        .identity("ChEBI:29103") \
        .is_part_of("extracellular", eUriType.LOCAL_URI)

# Potassium Ions
with annot_editor.new_physical_entity() as sink_potassium:
    sink_potassium \
        .about("sink_potassium", eUriType.LOCAL_URI) \
        .identity("ChEBI:29103") \
        .is_part_of("intracellular", eUriType.LOCAL_URI)

with annot_editor.new_physical_process() as charge_flowrate_potassium:
    charge_flowrate_potassium \
        .about("process_potassium", eUriType.LOCAL_URI) \
        .add_source("source_potassium", eUriType.LOCAL_URI, multiplier=1) \
        .add_sink("sink_potassium", eUriType.LOCAL_URI, multiplier=1) \
        .add_mediator("mediator_potassium_channel", eUriType.LOCAL_URI) \
        .has_property(property_about="potassium_channel.i_K", about_uri_type=eUriType.MODEL_URI, is_version_of="opb:OPB_00318")

#Leak Channel Process
# Leak channel activity (GO:0022840)
with annot_editor.new_physical_entity() as mediator_leak_channel:
    mediator_leak_channel \
        .about("mediator_leak_channel", eUriType.LOCAL_URI) \
        .identity("GO:0022840")

# Chloride and other Ions #ChEBI:17996 is Chloride Ion
with annot_editor.new_physical_entity() as source_leak:
    source_leak \
        .about("source_leak", eUriType.LOCAL_URI) \
        .identity("ChEBI:17996") \
        .is_part_of("extracellular", eUriType.LOCAL_URI)

# Chloride and other Ions #ChEBI:17996 is Chloride Ion
with annot_editor.new_physical_entity() as sink_leak:
    sink_leak \
        .about("sink_leak", eUriType.LOCAL_URI) \
        .identity("ChEBI:17996") \
        .is_part_of("intracellular", eUriType.LOCAL_URI)

with annot_editor.new_physical_process() as charge_flowrate_chloride:
    charge_flowrate_chloride \
        .about("process_leak", eUriType.LOCAL_URI) \
        .add_source("source_leak", eUriType.LOCAL_URI, multiplier=1) \
        .add_sink("sink_leak", eUriType.LOCAL_URI, multiplier=1) \
        .add_mediator("mediator_leak_channel", eUriType.LOCAL_URI) \
        .has_property(property_about="membrane.i_L", about_uri_type=eUriType.MODEL_URI, is_version_of="opb:OPB_00318")

print(rdf_graph_3_2_1)
# rdf_graph_3_2_1.draw("rdf_HodHux")