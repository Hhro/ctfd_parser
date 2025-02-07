import os
import shutil
from pathlib import Path
from urllib.parse import urljoin

class Manager(object):
    def __init__(self,ctfd,user,loc=''):
        self.ctfd=ctfd
        self.user=user
    
    def download_all_challenges_files(self):
        print("Download challenges files")
        base_url = self.ctfd.base_url
        ssid = self.user.session
        header = "Cookie: session={}".format(ssid)
        challenges = self.ctfd.challenges
        ctf_dir = self.ctfd.loc

        for chall_id in challenges.keys():
            chall = challenges[chall_id]
            chall_path = ctf_dir / chall['category'] / chall['name']
            chall_path.mkdir(parents=True,exist_ok=True)

            if chall['files'] == ['']:
                continue
            file_links = [urljoin(base_url,link) for link in chall['files']]

            for file_link in file_links:
                print("Download challenge file of [{}]{}".format(chall['category'].upper(),chall['name']))
                os.system("wget --header=\"{}\" --content-disposition -P \"{}\" \"{}\" 2>/dev/null".format(header,str(chall_path),file_link))
        
        print("Done")
        return True
    
    def add_all_challenges_description(self):
        print("Add descriptions of challenges")
        challenges = self.ctfd.challenges
        ctf_dir = self.ctfd.loc
        
        for chall_id in challenges.keys():
            chall = challenges[chall_id]
            chall_path = ctf_dir / chall['category'] / chall['name']
            chall_path.mkdir(parents=True,exist_ok=True)
            chall_path.touch("desc.md")

            chall_desc_path = chall_path / "desc.md"

            desc = "# {} \n\n---\n\n".format(chall['name'])
            desc += "Solves: {}\n\n".format(chall['solves'])
            desc += "{}".format(chall['description'])
            chall_desc_path.write_text(desc,encoding="utf-8")
        
        print("Done")
        return True








            

