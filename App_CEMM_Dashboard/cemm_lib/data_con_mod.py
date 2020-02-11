from cemm_lib import visual_rep_mod as visual

def dataset_url_manager(bol__enabled):
    try:
        print("\n -> dataset_url_manager() ...")
        if bol__enabled == True:
            #return visual.generate_table_v4(), print("\n -> dataset_url_manager() -> MESSAGE: Table Generated")
            return visual.generate_table_v4()
    except:
        return print("\n ***EXCEPION: -> dataset_url_manager() -> EXCEPION !")
