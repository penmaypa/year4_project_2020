from cemm_lib import visual_rep_mod as visual

def dataset_url_manager(bol__enable):
    try:
        print("\n -> dataset_url_manager() ...")
        if bol__enable == True:
            return visual.generate_table_v4("Rent in Dublin (url dataset)","https://data.smartdublin.ie/dataset/4997223b-13b2-4c97-9e88-cd94c6d35aec/resource/8c0f9bed-3b65-40c9-9bd2-505d7bdc1aeb/download/prtb-rents-ctdt.csv")
    except Exception as e:
        return print("\n ***EXCEPION: -> dataset_url_manager() -> EXCEPION !"), print(e)
