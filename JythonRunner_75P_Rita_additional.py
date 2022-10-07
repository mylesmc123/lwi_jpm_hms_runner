'''basin
Created on Oct 9, 2020

@author: MYMCMANUS-LOCAL
'''
# Instructions for running the HMS Jython Interpretor via the Windows Command Prompt here: https://www.hec.usace.army.mil/confluence/hmsdocs/hmsguides/running-hec-hms-with-jython  
# Example: cd /d C:/Programs/HEC-HMS-4.4
# hec-hms.cmd -script C:/jy/Runner.py

from hms.model import Project
from hms import Hms


# myProject = Project.open(r"Z:\Amite\HEC_HMS_RE-Calibration\HMS_Model_AORC_Hurricane_Rita\Amite_Final_HMS_Model.hms")

myProject = Project.open("Z:\Amite\HMS_Additional_Simulations\Rita\HMS_Models_Hurricanes_AORC_75Percentiles\Amite_Final_HMS_Model.hms")

runList = runList = [
    'Hurricane_Rita_75P_JPM_Sim501',
    'Hurricane_Rita_75P_JPM_Sim502',
    'Hurricane_Rita_75P_JPM_Sim503',
    'Hurricane_Rita_75P_JPM_Sim504',
    'Hurricane_Rita_75P_JPM_Sim505',
    'Hurricane_Rita_75P_JPM_Sim506',
    'Hurricane_Rita_75P_JPM_Sim507',
    'Hurricane_Rita_75P_JPM_Sim508',
    'Hurricane_Rita_75P_JPM_Sim509',
    'Hurricane_Rita_75P_JPM_Sim510',
    'Hurricane_Rita_75P_JPM_Sim511',
    'Hurricane_Rita_75P_JPM_Sim512',
    'Hurricane_Rita_75P_JPM_Sim513',
    'Hurricane_Rita_75P_JPM_Sim514',
    'Hurricane_Rita_75P_JPM_Sim515',
    'Hurricane_Rita_75P_JPM_Sim516',
    'Hurricane_Rita_75P_JPM_Sim517',
    'Hurricane_Rita_75P_JPM_Sim518',
    'Hurricane_Rita_75P_JPM_Sim519',
    'Hurricane_Rita_75P_JPM_Sim520',
    'Hurricane_Rita_75P_JPM_Sim521',
    'Hurricane_Rita_75P_JPM_Sim522',
    'Hurricane_Rita_75P_JPM_Sim523',
    'Hurricane_Rita_75P_JPM_Sim524',
    'Hurricane_Rita_75P_JPM_Sim525',
    'Hurricane_Rita_75P_JPM_Sim526',
    'Hurricane_Rita_75P_JPM_Sim527',
    'Hurricane_Rita_75P_JPM_Sim528',
    'Hurricane_Rita_75P_JPM_Sim529',
    'Hurricane_Rita_75P_JPM_Sim530',
    'Hurricane_Rita_75P_JPM_Sim531',
    'Hurricane_Rita_75P_JPM_Sim532',
    'Hurricane_Rita_75P_JPM_Sim533',
    'Hurricane_Rita_75P_JPM_Sim534',
    'Hurricane_Rita_75P_JPM_Sim535',
    'Hurricane_Rita_75P_JPM_Sim536',
    'Hurricane_Rita_75P_JPM_Sim537',
    'Hurricane_Rita_75P_JPM_Sim538',
    'Hurricane_Rita_75P_JPM_Sim539',
    'Hurricane_Rita_75P_JPM_Sim540',
    'Hurricane_Rita_75P_JPM_Sim541',
    'Hurricane_Rita_75P_JPM_Sim542',
    'Hurricane_Rita_75P_JPM_Sim543',
    'Hurricane_Rita_75P_JPM_Sim544',
    'Hurricane_Rita_75P_JPM_Sim545',
    'Hurricane_Rita_75P_JPM_Sim546',
    'Hurricane_Rita_75P_JPM_Sim547',
    'Hurricane_Rita_75P_JPM_Sim548',
    'Hurricane_Rita_75P_JPM_Sim549',
    'Hurricane_Rita_75P_JPM_Sim550',
    'Hurricane_Rita_75P_JPM_Sim551',
    'Hurricane_Rita_75P_JPM_Sim552',
    'Hurricane_Rita_75P_JPM_Sim553',
    'Hurricane_Rita_75P_JPM_Sim554',
    'Hurricane_Rita_75P_JPM_Sim555',
    'Hurricane_Rita_75P_JPM_Sim556',
    'Hurricane_Rita_75P_JPM_Sim557',
    'Hurricane_Rita_75P_JPM_Sim558',
    'Hurricane_Rita_75P_JPM_Sim559',
    'Hurricane_Rita_75P_JPM_Sim560',
    'Hurricane_Rita_75P_JPM_Sim561',
    'Hurricane_Rita_75P_JPM_Sim562',
    'Hurricane_Rita_75P_JPM_Sim563',
    'Hurricane_Rita_75P_JPM_Sim564',
    'Hurricane_Rita_75P_JPM_Sim565',
    'Hurricane_Rita_75P_JPM_Sim566',
    'Hurricane_Rita_75P_JPM_Sim567',
    'Hurricane_Rita_75P_JPM_Sim568',
    'Hurricane_Rita_75P_JPM_Sim569',
    'Hurricane_Rita_75P_JPM_Sim570',
    'Hurricane_Rita_75P_JPM_Sim571',
    'Hurricane_Rita_75P_JPM_Sim572',
    'Hurricane_Rita_75P_JPM_Sim573',
    'Hurricane_Rita_75P_JPM_Sim574',
    'Hurricane_Rita_75P_JPM_Sim575',
    'Hurricane_Rita_75P_JPM_Sim576',
    'Hurricane_Rita_75P_JPM_Sim577',
    'Hurricane_Rita_75P_JPM_Sim578',
    'Hurricane_Rita_75P_JPM_Sim579',
    'Hurricane_Rita_75P_JPM_Sim580',
    'Hurricane_Rita_75P_JPM_Sim581',
    'Hurricane_Rita_75P_JPM_Sim582',
    'Hurricane_Rita_75P_JPM_Sim583',
    'Hurricane_Rita_75P_JPM_Sim584',
    'Hurricane_Rita_75P_JPM_Sim585',
    'Hurricane_Rita_75P_JPM_Sim586',
    'Hurricane_Rita_75P_JPM_Sim587',
    'Hurricane_Rita_75P_JPM_Sim588',
    'Hurricane_Rita_75P_JPM_Sim589',
    'Hurricane_Rita_75P_JPM_Sim590',
    'Hurricane_Rita_75P_JPM_Sim591',
    'Hurricane_Rita_75P_JPM_Sim592',
    'Hurricane_Rita_75P_JPM_Sim593',
    'Hurricane_Rita_75P_JPM_Sim594',
    'Hurricane_Rita_75P_JPM_Sim595',
    'Hurricane_Rita_75P_JPM_Sim596',
    'Hurricane_Rita_75P_JPM_Sim597',
    'Hurricane_Rita_75P_JPM_Sim598',
    'Hurricane_Rita_75P_JPM_Sim599',
    'Hurricane_Rita_75P_JPM_Sim600',
    'Hurricane_Rita_75P_JPM_Sim601',
    'Hurricane_Rita_75P_JPM_Sim602',
    'Hurricane_Rita_75P_JPM_Sim603',
    'Hurricane_Rita_75P_JPM_Sim604',
    'Hurricane_Rita_75P_JPM_Sim605',
    'Hurricane_Rita_75P_JPM_Sim606',
    'Hurricane_Rita_75P_JPM_Sim607',
    'Hurricane_Rita_75P_JPM_Sim608',
    'Hurricane_Rita_75P_JPM_Sim609',
    'Hurricane_Rita_75P_JPM_Sim610',
    'Hurricane_Rita_75P_JPM_Sim611',
    'Hurricane_Rita_75P_JPM_Sim612',
    'Hurricane_Rita_75P_JPM_Sim613',
    'Hurricane_Rita_75P_JPM_Sim614',
    'Hurricane_Rita_75P_JPM_Sim615',
    'Hurricane_Rita_75P_JPM_Sim616',
    'Hurricane_Rita_75P_JPM_Sim617',
    'Hurricane_Rita_75P_JPM_Sim618',
    'Hurricane_Rita_75P_JPM_Sim619',
    'Hurricane_Rita_75P_JPM_Sim620',
    'Hurricane_Rita_75P_JPM_Sim621',
    'Hurricane_Rita_75P_JPM_Sim622',
    'Hurricane_Rita_75P_JPM_Sim623',
    'Hurricane_Rita_75P_JPM_Sim624',
    'Hurricane_Rita_75P_JPM_Sim625',
    'Hurricane_Rita_75P_JPM_Sim626',
    'Hurricane_Rita_75P_JPM_Sim627',
    'Hurricane_Rita_75P_JPM_Sim628',
    'Hurricane_Rita_75P_JPM_Sim629',
    'Hurricane_Rita_75P_JPM_Sim630',
    'Hurricane_Rita_75P_JPM_Sim631',
    'Hurricane_Rita_75P_JPM_Sim632',
    'Hurricane_Rita_75P_JPM_Sim633',
    'Hurricane_Rita_75P_JPM_Sim634',
    'Hurricane_Rita_75P_JPM_Sim635',
    'Hurricane_Rita_75P_JPM_Sim636',
    'Hurricane_Rita_75P_JPM_Sim637',
    'Hurricane_Rita_75P_JPM_Sim638',
    'Hurricane_Rita_75P_JPM_Sim639',
    'Hurricane_Rita_75P_JPM_Sim640',
    'Hurricane_Rita_75P_JPM_Sim641',
    'Hurricane_Rita_75P_JPM_Sim642',
    'Hurricane_Rita_75P_JPM_Sim643',
    'Hurricane_Rita_75P_JPM_Sim644',
    'Hurricane_Rita_75P_JPM_Sim645',
    'Hurricane_Rita_75P_JPM_Sim646',
    'Hurricane_Rita_75P_JPM_Sim647',
    'Hurricane_Rita_75P_JPM_Sim648',
    'Hurricane_Rita_75P_JPM_Sim649',
    'Hurricane_Rita_75P_JPM_Sim650',
    'Hurricane_Rita_75P_JPM_Sim651',
    'Hurricane_Rita_75P_JPM_Sim652',
    'Hurricane_Rita_75P_JPM_Sim653',
    'Hurricane_Rita_75P_JPM_Sim654',
    'Hurricane_Rita_75P_JPM_Sim655',
    'Hurricane_Rita_75P_JPM_Sim656',
    'Hurricane_Rita_75P_JPM_Sim657',
    'Hurricane_Rita_75P_JPM_Sim658',
    'Hurricane_Rita_75P_JPM_Sim659',
    'Hurricane_Rita_75P_JPM_Sim660',
    'Hurricane_Rita_75P_JPM_Sim661',
    'Hurricane_Rita_75P_JPM_Sim662',
    'Hurricane_Rita_75P_JPM_Sim663',
    'Hurricane_Rita_75P_JPM_Sim664',
    'Hurricane_Rita_75P_JPM_Sim665',
    'Hurricane_Rita_75P_JPM_Sim666',
    'Hurricane_Rita_75P_JPM_Sim667',
    'Hurricane_Rita_75P_JPM_Sim668',
    'Hurricane_Rita_75P_JPM_Sim669',
    'Hurricane_Rita_75P_JPM_Sim670',
    'Hurricane_Rita_75P_JPM_Sim671',
    'Hurricane_Rita_75P_JPM_Sim672',
    'Hurricane_Rita_75P_JPM_Sim673',
    'Hurricane_Rita_75P_JPM_Sim674',
    'Hurricane_Rita_75P_JPM_Sim675',
    'Hurricane_Rita_75P_JPM_Sim676',
    'Hurricane_Rita_75P_JPM_Sim677',
    'Hurricane_Rita_75P_JPM_Sim678',
    'Hurricane_Rita_75P_JPM_Sim679',
    'Hurricane_Rita_75P_JPM_Sim680',
    'Hurricane_Rita_75P_JPM_Sim681',
    'Hurricane_Rita_75P_JPM_Sim682',
    'Hurricane_Rita_75P_JPM_Sim683',
    'Hurricane_Rita_75P_JPM_Sim684',
    'Hurricane_Rita_75P_JPM_Sim685',
    'Hurricane_Rita_75P_JPM_Sim686',
    'Hurricane_Rita_75P_JPM_Sim687',
    'Hurricane_Rita_75P_JPM_Sim688',
    'Hurricane_Rita_75P_JPM_Sim689',
    'Hurricane_Rita_75P_JPM_Sim690',
    'Hurricane_Rita_75P_JPM_Sim691',
    'Hurricane_Rita_75P_JPM_Sim692',
    'Hurricane_Rita_75P_JPM_Sim693',
    'Hurricane_Rita_75P_JPM_Sim694',
    'Hurricane_Rita_75P_JPM_Sim695',
    'Hurricane_Rita_75P_JPM_Sim696',
    'Hurricane_Rita_75P_JPM_Sim697',
    'Hurricane_Rita_75P_JPM_Sim698',
    'Hurricane_Rita_75P_JPM_Sim699',
    'Hurricane_Rita_75P_JPM_Sim700',
    'Hurricane_Rita_75P_JPM_Sim701',
    'Hurricane_Rita_75P_JPM_Sim702',
    'Hurricane_Rita_75P_JPM_Sim703',
    'Hurricane_Rita_75P_JPM_Sim704',
    'Hurricane_Rita_75P_JPM_Sim705',
    'Hurricane_Rita_75P_JPM_Sim706',
    'Hurricane_Rita_75P_JPM_Sim707',
    'Hurricane_Rita_75P_JPM_Sim708',
    'Hurricane_Rita_75P_JPM_Sim709',
    'Hurricane_Rita_75P_JPM_Sim710',
    'Hurricane_Rita_75P_JPM_Sim711',
    'Hurricane_Rita_75P_JPM_Sim712',
    'Hurricane_Rita_75P_JPM_Sim713',
    'Hurricane_Rita_75P_JPM_Sim714',
    'Hurricane_Rita_75P_JPM_Sim715',
    'Hurricane_Rita_75P_JPM_Sim716',
    'Hurricane_Rita_75P_JPM_Sim717',
    'Hurricane_Rita_75P_JPM_Sim718',
    'Hurricane_Rita_75P_JPM_Sim719',
    'Hurricane_Rita_75P_JPM_Sim720',
    'Hurricane_Rita_75P_JPM_Sim721',
    'Hurricane_Rita_75P_JPM_Sim722',
    'Hurricane_Rita_75P_JPM_Sim723',
    'Hurricane_Rita_75P_JPM_Sim724',
    'Hurricane_Rita_75P_JPM_Sim725',
    'Hurricane_Rita_75P_JPM_Sim726',
    'Hurricane_Rita_75P_JPM_Sim727',
    'Hurricane_Rita_75P_JPM_Sim728',
    'Hurricane_Rita_75P_JPM_Sim729',
    'Hurricane_Rita_75P_JPM_Sim730',
    'Hurricane_Rita_75P_JPM_Sim731',
    'Hurricane_Rita_75P_JPM_Sim732',
    'Hurricane_Rita_75P_JPM_Sim733',
    'Hurricane_Rita_75P_JPM_Sim734',
    'Hurricane_Rita_75P_JPM_Sim735',
    'Hurricane_Rita_75P_JPM_Sim736',
    'Hurricane_Rita_75P_JPM_Sim737',
    'Hurricane_Rita_75P_JPM_Sim738',
    'Hurricane_Rita_75P_JPM_Sim739',
    'Hurricane_Rita_75P_JPM_Sim740',
    'Hurricane_Rita_75P_JPM_Sim741',
    'Hurricane_Rita_75P_JPM_Sim742',
    'Hurricane_Rita_75P_JPM_Sim743',
    'Hurricane_Rita_75P_JPM_Sim744',
    'Hurricane_Rita_75P_JPM_Sim745',
    'Hurricane_Rita_75P_JPM_Sim746',
    'Hurricane_Rita_75P_JPM_Sim747',
    'Hurricane_Rita_75P_JPM_Sim748',
    'Hurricane_Rita_75P_JPM_Sim749',
    'Hurricane_Rita_75P_JPM_Sim750',
    'Hurricane_Rita_75P_JPM_Sim751',
    'Hurricane_Rita_75P_JPM_Sim752',
    'Hurricane_Rita_75P_JPM_Sim753',
    'Hurricane_Rita_75P_JPM_Sim754',
    'Hurricane_Rita_75P_JPM_Sim755',
    'Hurricane_Rita_75P_JPM_Sim756',
    'Hurricane_Rita_75P_JPM_Sim757',
    'Hurricane_Rita_75P_JPM_Sim758',
    'Hurricane_Rita_75P_JPM_Sim759',
    'Hurricane_Rita_75P_JPM_Sim760',
    'Hurricane_Rita_75P_JPM_Sim761',
    'Hurricane_Rita_75P_JPM_Sim762',
    'Hurricane_Rita_75P_JPM_Sim763',
    'Hurricane_Rita_75P_JPM_Sim764',
    'Hurricane_Rita_75P_JPM_Sim765',
    'Hurricane_Rita_75P_JPM_Sim766',
    'Hurricane_Rita_75P_JPM_Sim767',
    'Hurricane_Rita_75P_JPM_Sim768',
    'Hurricane_Rita_75P_JPM_Sim769',
    'Hurricane_Rita_75P_JPM_Sim770',
    'Hurricane_Rita_75P_JPM_Sim771',
    'Hurricane_Rita_75P_JPM_Sim772',
    'Hurricane_Rita_75P_JPM_Sim773',
    'Hurricane_Rita_75P_JPM_Sim774',
    'Hurricane_Rita_75P_JPM_Sim775',
    'Hurricane_Rita_75P_JPM_Sim776',
    'Hurricane_Rita_75P_JPM_Sim777',
    'Hurricane_Rita_75P_JPM_Sim778',
    'Hurricane_Rita_75P_JPM_Sim779',
    'Hurricane_Rita_75P_JPM_Sim780',
    'Hurricane_Rita_75P_JPM_Sim781',
    'Hurricane_Rita_75P_JPM_Sim782',
    'Hurricane_Rita_75P_JPM_Sim783',
    'Hurricane_Rita_75P_JPM_Sim784',
    'Hurricane_Rita_75P_JPM_Sim785',
    'Hurricane_Rita_75P_JPM_Sim786',
    'Hurricane_Rita_75P_JPM_Sim787',
    'Hurricane_Rita_75P_JPM_Sim788',
    'Hurricane_Rita_75P_JPM_Sim789',
    'Hurricane_Rita_75P_JPM_Sim790',
    'Hurricane_Rita_75P_JPM_Sim791',
    'Hurricane_Rita_75P_JPM_Sim792',
    'Hurricane_Rita_75P_JPM_Sim793',
    'Hurricane_Rita_75P_JPM_Sim794',
    'Hurricane_Rita_75P_JPM_Sim795',
    'Hurricane_Rita_75P_JPM_Sim796',
    'Hurricane_Rita_75P_JPM_Sim797',
    'Hurricane_Rita_75P_JPM_Sim798',
    'Hurricane_Rita_75P_JPM_Sim799',
    'Hurricane_Rita_75P_JPM_Sim800',
    'Hurricane_Rita_75P_JPM_Sim801',
    'Hurricane_Rita_75P_JPM_Sim802',
    'Hurricane_Rita_75P_JPM_Sim803',
    'Hurricane_Rita_75P_JPM_Sim804',
    'Hurricane_Rita_75P_JPM_Sim805',
    'Hurricane_Rita_75P_JPM_Sim806',
    'Hurricane_Rita_75P_JPM_Sim807',
    'Hurricane_Rita_75P_JPM_Sim808',
    'Hurricane_Rita_75P_JPM_Sim809',
    'Hurricane_Rita_75P_JPM_Sim810',
    'Hurricane_Rita_75P_JPM_Sim811',
    'Hurricane_Rita_75P_JPM_Sim812',
    'Hurricane_Rita_75P_JPM_Sim813',
    'Hurricane_Rita_75P_JPM_Sim814',
    'Hurricane_Rita_75P_JPM_Sim815',
    'Hurricane_Rita_75P_JPM_Sim816',
    'Hurricane_Rita_75P_JPM_Sim817',
    'Hurricane_Rita_75P_JPM_Sim818',
    'Hurricane_Rita_75P_JPM_Sim819',
    'Hurricane_Rita_75P_JPM_Sim820',
    'Hurricane_Rita_75P_JPM_Sim821',
    'Hurricane_Rita_75P_JPM_Sim822',
    'Hurricane_Rita_75P_JPM_Sim823',
    'Hurricane_Rita_75P_JPM_Sim824',
    'Hurricane_Rita_75P_JPM_Sim825',
    'Hurricane_Rita_75P_JPM_Sim826',
    'Hurricane_Rita_75P_JPM_Sim827',
    'Hurricane_Rita_75P_JPM_Sim828',
    'Hurricane_Rita_75P_JPM_Sim829',
    'Hurricane_Rita_75P_JPM_Sim830',
    'Hurricane_Rita_75P_JPM_Sim831',
    'Hurricane_Rita_75P_JPM_Sim832',
    'Hurricane_Rita_75P_JPM_Sim833',
    'Hurricane_Rita_75P_JPM_Sim834',
    'Hurricane_Rita_75P_JPM_Sim835',
    'Hurricane_Rita_75P_JPM_Sim836',
    'Hurricane_Rita_75P_JPM_Sim837',
    'Hurricane_Rita_75P_JPM_Sim838',
    'Hurricane_Rita_75P_JPM_Sim839',
    'Hurricane_Rita_75P_JPM_Sim840',
    'Hurricane_Rita_75P_JPM_Sim841',
    'Hurricane_Rita_75P_JPM_Sim842',
    'Hurricane_Rita_75P_JPM_Sim843',
    'Hurricane_Rita_75P_JPM_Sim844',
    'Hurricane_Rita_75P_JPM_Sim845',
    'Hurricane_Rita_75P_JPM_Sim846',
    'Hurricane_Rita_75P_JPM_Sim847',
    'Hurricane_Rita_75P_JPM_Sim848',
    'Hurricane_Rita_75P_JPM_Sim849',
    'Hurricane_Rita_75P_JPM_Sim850',
    'Hurricane_Rita_75P_JPM_Sim851',
    'Hurricane_Rita_75P_JPM_Sim852',
    'Hurricane_Rita_75P_JPM_Sim853',
    'Hurricane_Rita_75P_JPM_Sim854',
    'Hurricane_Rita_75P_JPM_Sim855',
    'Hurricane_Rita_75P_JPM_Sim856',
    'Hurricane_Rita_75P_JPM_Sim857',
    'Hurricane_Rita_75P_JPM_Sim858',
    'Hurricane_Rita_75P_JPM_Sim859',
    'Hurricane_Rita_75P_JPM_Sim860',
    'Hurricane_Rita_75P_JPM_Sim861',
    'Hurricane_Rita_75P_JPM_Sim862',
    'Hurricane_Rita_75P_JPM_Sim863',
    'Hurricane_Rita_75P_JPM_Sim864',
    'Hurricane_Rita_75P_JPM_Sim865',
    'Hurricane_Rita_75P_JPM_Sim866',
    'Hurricane_Rita_75P_JPM_Sim867',
    'Hurricane_Rita_75P_JPM_Sim868',
    'Hurricane_Rita_75P_JPM_Sim869',
    'Hurricane_Rita_75P_JPM_Sim870',
    'Hurricane_Rita_75P_JPM_Sim871',
    'Hurricane_Rita_75P_JPM_Sim872',
    'Hurricane_Rita_75P_JPM_Sim873',
    'Hurricane_Rita_75P_JPM_Sim874',
    'Hurricane_Rita_75P_JPM_Sim875',
    'Hurricane_Rita_75P_JPM_Sim876',
    'Hurricane_Rita_75P_JPM_Sim877',
    'Hurricane_Rita_75P_JPM_Sim878',
    'Hurricane_Rita_75P_JPM_Sim879',
    'Hurricane_Rita_75P_JPM_Sim880',
    'Hurricane_Rita_75P_JPM_Sim881',
    'Hurricane_Rita_75P_JPM_Sim882',
    'Hurricane_Rita_75P_JPM_Sim883',
    'Hurricane_Rita_75P_JPM_Sim884',
    'Hurricane_Rita_75P_JPM_Sim885',
    'Hurricane_Rita_75P_JPM_Sim886',
    'Hurricane_Rita_75P_JPM_Sim887',
    'Hurricane_Rita_75P_JPM_Sim888',
    'Hurricane_Rita_75P_JPM_Sim889',
    'Hurricane_Rita_75P_JPM_Sim890',
    'Hurricane_Rita_75P_JPM_Sim891',
    'Hurricane_Rita_75P_JPM_Sim892',
    'Hurricane_Rita_75P_JPM_Sim893',
    'Hurricane_Rita_75P_JPM_Sim894',
    'Hurricane_Rita_75P_JPM_Sim895',
    'Hurricane_Rita_75P_JPM_Sim896',
    'Hurricane_Rita_75P_JPM_Sim897',
    'Hurricane_Rita_75P_JPM_Sim898',
    'Hurricane_Rita_75P_JPM_Sim899',
    'Hurricane_Rita_75P_JPM_Sim900',
    'Hurricane_Rita_75P_JPM_Sim901',
    'Hurricane_Rita_75P_JPM_Sim902',
    'Hurricane_Rita_75P_JPM_Sim903',
    'Hurricane_Rita_75P_JPM_Sim904',
    'Hurricane_Rita_75P_JPM_Sim905',
    'Hurricane_Rita_75P_JPM_Sim906',
    'Hurricane_Rita_75P_JPM_Sim907',
    'Hurricane_Rita_75P_JPM_Sim908',
    'Hurricane_Rita_75P_JPM_Sim909',
    'Hurricane_Rita_75P_JPM_Sim910',
    'Hurricane_Rita_75P_JPM_Sim911',
    'Hurricane_Rita_75P_JPM_Sim912',
    'Hurricane_Rita_75P_JPM_Sim913',
    'Hurricane_Rita_75P_JPM_Sim914',
    'Hurricane_Rita_75P_JPM_Sim915',
    'Hurricane_Rita_75P_JPM_Sim916',
    'Hurricane_Rita_75P_JPM_Sim917',
    'Hurricane_Rita_75P_JPM_Sim918',
    'Hurricane_Rita_75P_JPM_Sim919',
    'Hurricane_Rita_75P_JPM_Sim920',
    'Hurricane_Rita_75P_JPM_Sim921',
    'Hurricane_Rita_75P_JPM_Sim922',
    'Hurricane_Rita_75P_JPM_Sim923',
    'Hurricane_Rita_75P_JPM_Sim924',
    'Hurricane_Rita_75P_JPM_Sim925',
    'Hurricane_Rita_75P_JPM_Sim926',
    'Hurricane_Rita_75P_JPM_Sim927',
    'Hurricane_Rita_75P_JPM_Sim928',
    'Hurricane_Rita_75P_JPM_Sim929',
    'Hurricane_Rita_75P_JPM_Sim930',
    'Hurricane_Rita_75P_JPM_Sim931',
    'Hurricane_Rita_75P_JPM_Sim932',
    'Hurricane_Rita_75P_JPM_Sim933',
    'Hurricane_Rita_75P_JPM_Sim934',
    'Hurricane_Rita_75P_JPM_Sim935',
    'Hurricane_Rita_75P_JPM_Sim936',
    'Hurricane_Rita_75P_JPM_Sim937',
    'Hurricane_Rita_75P_JPM_Sim938',
    'Hurricane_Rita_75P_JPM_Sim939',
    'Hurricane_Rita_75P_JPM_Sim940',
    'Hurricane_Rita_75P_JPM_Sim941',
    'Hurricane_Rita_75P_JPM_Sim942',
    'Hurricane_Rita_75P_JPM_Sim943',
    'Hurricane_Rita_75P_JPM_Sim944',
    'Hurricane_Rita_75P_JPM_Sim945',
    'Hurricane_Rita_75P_JPM_Sim946',
    'Hurricane_Rita_75P_JPM_Sim947',
    'Hurricane_Rita_75P_JPM_Sim948',
    'Hurricane_Rita_75P_JPM_Sim949',
    'Hurricane_Rita_75P_JPM_Sim950',
    'Hurricane_Rita_75P_JPM_Sim951',
    'Hurricane_Rita_75P_JPM_Sim952',
    'Hurricane_Rita_75P_JPM_Sim953',
    'Hurricane_Rita_75P_JPM_Sim954',
    'Hurricane_Rita_75P_JPM_Sim955',
    'Hurricane_Rita_75P_JPM_Sim956',
    'Hurricane_Rita_75P_JPM_Sim957',
    'Hurricane_Rita_75P_JPM_Sim958',
    'Hurricane_Rita_75P_JPM_Sim959',
    'Hurricane_Rita_75P_JPM_Sim960',
    'Hurricane_Rita_75P_JPM_Sim961',
    'Hurricane_Rita_75P_JPM_Sim962',
    'Hurricane_Rita_75P_JPM_Sim963',
    'Hurricane_Rita_75P_JPM_Sim964',
    'Hurricane_Rita_75P_JPM_Sim965',
    'Hurricane_Rita_75P_JPM_Sim966',
    'Hurricane_Rita_75P_JPM_Sim967',
    'Hurricane_Rita_75P_JPM_Sim968',
    'Hurricane_Rita_75P_JPM_Sim969',
    'Hurricane_Rita_75P_JPM_Sim970',
    'Hurricane_Rita_75P_JPM_Sim971',
    'Hurricane_Rita_75P_JPM_Sim972',
    'Hurricane_Rita_75P_JPM_Sim973',
    'Hurricane_Rita_75P_JPM_Sim974',
    'Hurricane_Rita_75P_JPM_Sim975',
    'Hurricane_Rita_75P_JPM_Sim976',
    'Hurricane_Rita_75P_JPM_Sim977',
    'Hurricane_Rita_75P_JPM_Sim978',
    'Hurricane_Rita_75P_JPM_Sim979',
    'Hurricane_Rita_75P_JPM_Sim980',
    'Hurricane_Rita_75P_JPM_Sim981',
    'Hurricane_Rita_75P_JPM_Sim982',
    'Hurricane_Rita_75P_JPM_Sim983',
    'Hurricane_Rita_75P_JPM_Sim984',
    'Hurricane_Rita_75P_JPM_Sim985',
    'Hurricane_Rita_75P_JPM_Sim986',
    'Hurricane_Rita_75P_JPM_Sim987',
    'Hurricane_Rita_75P_JPM_Sim988',
    'Hurricane_Rita_75P_JPM_Sim989',
    'Hurricane_Rita_75P_JPM_Sim990',
    'Hurricane_Rita_75P_JPM_Sim991',
    'Hurricane_Rita_75P_JPM_Sim992',
    'Hurricane_Rita_75P_JPM_Sim993',
    'Hurricane_Rita_75P_JPM_Sim994',
    'Hurricane_Rita_75P_JPM_Sim995',
    'Hurricane_Rita_75P_JPM_Sim996',
    'Hurricane_Rita_75P_JPM_Sim997',
    'Hurricane_Rita_75P_JPM_Sim998',
    'Hurricane_Rita_75P_JPM_Sim999',
    'Hurricane_Rita_75P_JPM_Sim1000'
]

for run in runList:
    myProject.computeRun(run)

myProject.close()

Hms.shutdownEngine()