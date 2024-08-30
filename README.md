
Configuration of a Local Software to Azure Cloud Environment
(Repository for my thesis work)



In this bachelor’s thesis work, a server-side program of a warehouse stock manage-
ment system that is used in Metropolia UAS industrial testing environment was up-
dated using Django REST Framework, and uploaded and configured to Microsoft
Azure, a public cloud service environment, from a local hosted closed server.
The purpose of this work was to demonstrate the potential possibilities of web tech-
nologies and cloud services in modernization of automation systems. The secondary
purpose was to create a guidance to showcase how the said web technologies could
be used in the industrial field.

The work was phased in a manner of continuous integration, where small parts of
working code were published to cloud at a time. The program was also separated
into many Azure services: Web App Service handles the requests done by the
browser, PostgreSQL Database stores the data to cloud database, and IoT Hub de-
livers the requests to mechatronic warehouse robots application interface. The final
product uses HTTP communication protocol between browser and web application,
while MQTT between web application and PLC. The project is limited to showcasing
the connection of Web App to IoT Hub, while for the final production, the PLC needs
to be connected as well using the same methodology showcased in this document.
The final product was met with the goals set for the thesis work, although the final
connection to the mechatronic warehouse was left missing. The report gives the
reader an overview of cloud services, and one demonstrative example of how those
could be used in industrial automation systems. Although the project is showcased in
a consequent manner in this documentation, each chapter discusses only one certain
part of this project at a time, giving informative demonstration of each step of the pro-
ject, to understand the concept being discussed.

Keywords: Cloud Services, Azure, Python, Automation


Full thesis documentation in finnish: https://urn.fi/URN:NBN:fi:amk-2024052716055
