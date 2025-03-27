# Piekluves_Darbs
**p2-exam-darbs**

**Problēma** - Viens pusaudzis grib nopirkt jaunu spēles konsoli un piemērotu elektronikas sīkrīku. Pusaudzis atrod pieejamu jaunu spēles konsoli plauktā, bet RD Electornics un citu elektronikas veikalos Ventspilī nav piemērotāka elektronikas sīkrīku. Pusaudzis apmeklē internetveikalā un uzzināja, ka ir pieejams sīkrīks Rīgā, nevis Ventspilī. Ventspilī nav plašāki piemērotāki elektronikas veikali. Cilvēki ceļo uz galvaspilsētu Rīga un citās pilsētās tikai fiziskos elektronikas veikalos dēļ. Cilvēki tērē piegādes cenas un gaida pāris dienas, lai dabūtu savu produktu rokās.

**Risinājums** 
	- _Reklamēšu jaunu elektronikas veikalu, izmantojot aplikāciju_
	- _lietotājs var piereģistrēties, sameklēt pieejamu elektronisko sīkrīku_
	- _noklikšķinot uz programmas ieejamo saiti, lietotājs tiek ielikts uz oriģinālo veikala mājaslapu_

**Mērķauditorija** - Cilvēki, biežāk pusaudži, kuri grib aiziet un nopirkt savu preci netālu (5min) no savas mājas.
## Programmas Prasību Specifikācijas

**Funkcionālās prasības** - izmantošu pieejamās GUI bibliotēkas (Tkinter), programmu kodus (Python), API funkciju (atrašanas vieta veikalā) un Datubāzi, kas saglabā starptautiskās elektronikas preces. Kā arī izmantošu datubāzi, lai saglabā lietotāja informāciju un vēsturi ar sameklētām precēm.

**Lietotāja saskarnes dizains** - Lietotāja pirmā cilnes vizualizācija būs reģistrēšanās (lietotāja vārds un parole, kas saglabās to datus), lietotājam ir arī iespēja ieiet uz viesa režīmu, kas nesaglabā lietotāja sameklētās preces vēsturi. Pēc šis cilnes, lietotājam būs izvēle noklikšķināt uz trim pogām:
1. _preces meklēšana poga, lai lietotājs var brīvi ievadīt un sameklēt savu ievēloto preci_
2. _rekomendācijas poga ar ko izmantos lietotāja nesen meklētās preces datus un izmantos tos datus, lai ar vizualizāciju parāda šo preces attēlu, kad iespied pogu "rekomendācija" (PS: ši poga tikai parādīsies, kad lietotājs ievada savu ievēloto preci uz "preces meklēšana" pogā, kad datubāze saglabā lietotāja darbību)_
3. _saites kontaktinformācija, kur ir pievienots veikalas atrašanas vieta un telefona numurs, lai lietotājs var sazināties ar veikala vadītāja_

papildināts ar vizualizācijas plakātu, kas reklamē mērķauditoriju par unikāli importētam elektonikas preču sīkrīkus.

**Tehniskās prasības** - tīkls ir izveidots prekš Windows operātorsistēma.
