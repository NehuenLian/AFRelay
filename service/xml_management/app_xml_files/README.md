# `app_xml_files/` Folder

This folder is used internally by the web service to access XML files needed to send information.  

- loginTicketRequest.xml
- loginTicketResponse.xml

Files placed in the host folder `host_xml/` are mounted here as a Docker volume.  

For security reasons, these files are excluded from the repository using `.gitignore`.

⚠️ **Never upload these files to GitHub.**
