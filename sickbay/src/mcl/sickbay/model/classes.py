# encoding: utf-8
#

'''Classes'''

from sqlalchemy.ext.declarative import delcarative_base
from sqlalchemy import Column, Integer, String, Boolean, Float, Date


_base = delcarative_base()


class ClinicalCore(_base):
    '''🩺 Core clinical data; this has a 1-to-many relationship with the rest of the world'''

    __tablename__ = 'ClinicalCore'

    partcipant_ID                      = Column(String(16), primary_key=True)
    anchor_type                        = Column(String)
    days_to_consent                    = Column(Integer)
    days_to_enrollment                 = Column(Integer)
    gender                             = Column(String(24))
    ethnicity                          = Column(String(32))
    race                               = Column(String)
    vital_status                       = Column(String)
    days_to_vital_status_reference     = Column(Integer)
    age_at_index                       = Column(Integer)
    days_to_birth                      = Column(Integer)
    year_of_birth                      = Column(Integer)
    education                          = Column(String)
    income                             = Column(String)
    height                             = Column(Integer)
    height_uom                         = Column(String)
    days_to_weight_recorded            = Column(Integer)
    weight                             = Column(Integer)
    weight_uom                         = Column(String)
    prior_cancer                       = Column(String(8))
    current_lesion_type                = Column(String)
    days_to_diagnosis                  = Column(Integer)
    year_of_diagnosis                  = Column(Integer)
    age_at_diagnosis                   = Column(Integer)
    how_detected                       = Column(String)
    days_to_detection_date             = Column(Integer)
    days_to_last_screen_date           = Column(Integer)
    days_to_last_neg_screen_date       = Column(Integer)
    mode_of_detection                  = Column(String(32))
    lesion_type                        = Column(String)
    specimen_collected                 = Column(Boolean)
    age_at_menses_start                = Column(Integer)
    menses_stop                        = Column(Integer)
    age_at_menses_stop                 = Column(Integer)
    biomarker_tested                   = Column(Boolean)
    relative_with_cancer_history       = Column(Boolean)
    relative_with_cancer_history_count = Column(Integer)
    tobacco_smoking_status             = Column(String)
    type_tobacco_used                  = Column(String)
    tobacco_smoking_onset_age          = Column(Integer)
    tobacco_smoking_quit_age           = Column(Integer)
    years_smoked                       = Column(Integer)
    cigarettes_per_day                 = Column(Integer)
    alcohol_history                    = Column(Boolean)
    alcohol_drinks_per_day             = Column(Integer)
    alcohol_days_per_week              = Column(Integer)


class Organ(_base):
    '''♥️ This is the generic base class common to all organs.'''

    __tablename__ = 'Organ'

    partcipant_ID = Column(String(16), primary_key=True)
    anchor_type = Column(String)

    # 🤷‍♀️ What other generic attributes are common between all organs?


class BreastOrgan(Organ):
    '''Breast-specific data'''

    __tablename__ = 'BreastOrgan'

    laterality                            = Column(String(16))
    site                                  = Column(String(16))
    size                                  = Column(Integer)
    necrosis                              = Column(Boolean)
    necrosis_location                     = Column(String)
    surgical_margin                       = Column(String)
    recurrence                            = Column(Boolean)
    pathologic_T_stage_7                  = Column(String)
    pathologic_N_stage_7                  = Column(String)
    pathologic_M_stage_7                  = Column(String)
    clinical_T_stage_7                    = Column(String)
    clinical_N_stage_7                    = Column(String)
    clinical_M_stage_7                    = Column(String)
    disease_stage_7                       = Column(String)
    path_TNM_class_T_8                    = Column(String)
    path_TNM_class_N_8                    = Column(String)
    path_TNM_class_M_8                    = Column(String)
    clinical_TNM_class_T_8                = Column(String)
    clinical_TNM_class_N_8                = Column(String)
    clinical_TNM_class_M_8                = Column(String)
    disease_stage_ajcc_8                  = Column(String)
    genetic_testing                       = Column(String)
    BRCA1                                 = Column(Boolean)
    BRCA2                                 = Column(Boolean)
    estrogen_receptor                     = Column(String)
    ER_percent_positivity                 = Column(Integer)
    progesterone_receptor                 = Column(String)
    HER2_immunohistochemistry             = Column(String)
    HER2_in_situ_hybridization            = Column(String)
    Ki_67_percent_positive_nuclei         = Column(String)
    menopausal_status                     = Column(String)
    ECOG_score                            = Column(Integer)
    method_of_detection                   = Column(String)
    days_to_detection_date                = Column(Integer)
    days_to_last_screening_mammo          = Column(Integer)
    days_to_last_negative_screening_mammo = Column(Integer)
    detected_between_screening_intervals  = Column(Boolean)
    multifocal_disease                    = Column(String)
    multicentric_disease                  = Column(Boolean)
    imaging_workup                        = Column(String)
    BIRADS_density                        = Column(String)


class ProstateOrgan(Organ):
    '''Prostate-specific data'''
    __tablename__ = 'ProstateOrgan'
    # Add prostate-specific attributes here


# Add other organs here


class Biospecmen(_base):
    '''🧪 Biological specimen data'''

    __tablename__ = 'Biospecimen'

    specimen_ID                 = Column(String(32), primary_key=True)
    specimen_id_local           = Column(String)
    partcipant_ID               = Column(String(16))
    adjacent_specimen_id        = Column(String)  # 🔧 FIXME: This is a ``|`` separated list; should be a separate table
    specimen_type               = Column(String)
    anatomical_site             = Column(String)
    tumor_tissue_type           = Column(String)
    precancer_type              = Column(String)
    precancer_type_other        = Column(String)
    specimen_laterality         = Column(String)
    acquisition_method          = Column(String)
    acquisition_method_other    = Column(String)
    days_to_collection          = Column(Integer)
    time_excision_to_processing = Column(Integer)
    ischemic_time               = Column(Integer)
    portion_weight              = Column(Float)
    total_volume                = Column(Float)
    preservation_method         = Column(String)  # 🔧 FIXME: should be enumerated
    preservation_method_other   = Column(String)
    fixative_used               = Column(String)  # 🔧 FIXME: should be enumerated
    fixative_other              = Column(String)
    fixation_duration           = Column(Integer)
    processing_duration         = Column(Integer)
    analyte_type                = Column(String)
    analyte_type_other          = Column(String)  # 🔧 FIXME: should be enumerated
    protocol_number             = Column(Integer)
    protocol_version            = Column(Integer)
    storage_method              = Column(String)  # 🔧 FIXME: should be enumerated
    storage_method_other        = Column(String)
    days_to_storage             = Column(Integer)
    slide_charge_type           = Column(String)
    section_thickness           = Column(Integer)
    days_to_shipping            = Column(Integer)
    shipping_conditions         = Column(String)
    shipping_destination        = Column(String)


class Genomics(_base):
    '''🧬 Structure, function, evolution, and mapping of genome data'''

    __tablename__ = 'Genomics'

    partcipant_ID                    = Column(String(16))
    filename                         = Column(String)
    dateFileGenerated                = Column(Date)
    siteID                           = Column(Integer)
    submittingInvestigatorID         = Column(Integer)
    processingLevel                  = Column(String)
    fileType                         = Column(String)
    md5sum                           = Column(Integer)
    specimen_id                      = Column(String)
    sequencing_center                = Column(Integer)
    sequencing_date                  = Column(Date)
    sequencing_batch_id              = Column(String)
    library_name                     = Column(String)
    library_strategy                 = Column(String)
    library_source                   = Column(String)
    library_selection                = Column(String)
    library_strand                   = Column(String)
    library_layout                   = Column(Boolean)
    sequencing_platform              = Column(String)
    read_length                      = Column(Integer)
    rin                              = Column(Integer)
    adapter_name                     = Column(String)
    adapter_sequence                 = Column(String)
    flow_cell_barcode                = Column(String)
    size_selection_range             = Column(String)
    target_capture_kit_target_region = Column(String)
    input_type                       = Column(String)
    number_PCR_cycles                = Column(Integer)
    number_libraries_in_pool         = Column(Integer)
    index_sequence                   = Column(String)
    indexing_type                    = Column(String)  # 🔧 FIXME: should be enumerated
    indexing_type_other              = Column(String)


class Imaging(_base):
    '''🖼 Imaging'''

    __tablename__ = 'Imaging'

    partcipant_ID = Column(String(16))

    # ☑️ TODO: What else goes here?
