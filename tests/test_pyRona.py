#!/usr/bin/python3
# Copyright 2016 Francisco Pina Martins <f.pinamartins@gmail.com>
# This file is part of pyRona.
# pyRona is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# pyRona is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with pyRona.  If not, see <http://www.gnu.org/licenses/>.

import pytest
import pickle
import numpy as np
import pyRona.pyRona.pyRona as pr
from collections import defaultdict

# Initiatize the Rona class

with open("tests/data/jar/file_parser.popnames_parser.pickle","rb") as f:
    pr.RonaClass.POP_NAMES = pickle.load(f)

ronas = {}

rona = pr.RonaClass("5")
rona_dict = {'558': [0.0014018084856003402, 0.00044007391611439851, 5.4391158171442511e-05, 0.00076889319051446367, 0.0012089671066288572, 0.0012905538438860258, 0.00044007391611439851, 0.00024723253714292048, 0.00016564579988575674, 0.00022003695805716098, 0.0003560148534858055, 0.001649041022743251, 0.0023907386341719839, 0.00076889319051452103, 0.0014561996437717636, 0.000192841378971478], '917': [0.034081182741242728, 0.010699207280319563, 0.0013223739335225977, 0.018693558787524652, 0.029392766067844217, 0.031376326968128254, 0.010699207280319563, 0.0060107906069210527, 0.0040272297066371275, 0.0053496036401597816, 0.00865553847396636, 0.040091973348163668, 0.058124345168927158, 0.018693558787524652, 0.035403556674765267, 0.004688416673398455], '928': [0.0083601552048518327, 0.015616386870309709, 0.0019301152311618597, 0.027284810767788412, 0.042901197638098118, 0.045796370484840906, 0.015616386870309709, 0.0087732510507357846, 0.0058780782039929945, 0.0078081934351548546, 0.012633481513059503, 0.058517584508407702, 0.084837337660615311, 0.027284810767788412, 0.051674448688833904, 0.0068431358195739245], '1061': [0.010428942606976906, 0.0032739890371108844, 0.00040465033042942443, 0.0057202842165252595, 0.0089942732536361439, 0.0096012487492803129, 0.0032739890371108844, 0.0018393196837702072, 0.0012323441881260389, 0.0016369945185554632, 0.0026486203446290349, 0.012268262290747071, 0.017786221342057564, 0.0057202842165252179, 0.010833592937406331, 0.0014346693533407616]}
rona.pop_ronas = defaultdict(list)
for k,v in rona_dict.items():
    rona.pop_ronas[k] = v
rona.corr_coef = {'558': 0.00030210072963844631, '917': 0.19358706622191832, '928': 0.27211499170048115, '1061': 0.017094197215003121}
rona.avg_ronas = [0.018735931355473877, 0.013199755733777314, 0.0016314304839499785, 0.023062494568566048, 0.036262250302343361, 0.038709396028268381, 0.013199755733777314, 0.0074155931088636358, 0.0049684473829386556, 0.0065998778668886569, 0.010678454076763636, 0.049462006036120554, 0.071708785362711747, 0.023062494568566048, 0.043677843411207, 0.0057841626249136571]
rona.stderr_ronas = [0.0061531608283148442, 0.0029980427796045179, 0.00037054461320954265, 0.0052381533958258866, 0.008236196175430404, 0.0087920130952447249, 0.0029980427796045179, 0.001684293696407024, 0.0011284767765927107, 0.0014990213898022629, 0.0024253829228261183, 0.01123423895503489, 0.016287120044256045, 0.0052381533958258822, 0.0099204898718374332, 0.0013137490831974829]
ronas['5'] = rona

rona = pr.RonaClass("11")
rona_dict = {'109': [0.0088246354874106526, 0.027885848140217651, 0.006249038485830795, 0.0075278627810403476, 0.0058167809170407035, 0.0081934496949213342, 0.0050195723213135417, 0.0068144134373971212, 0.0065646313820755019, 0.005800328206809916, 0.0050360250315443457, 0.0075622639024319196, 0.0083265670776975064, 0.0034468915738891386, 0.0065152732513832018, 0.0067964650262362734], '145': [0.025307793158957186, 0.44069278775643461, 0.098756407811970787, 0.11896625191901598, 0.091925244131343786, 0.074627513461562239, 0.07932659277572375, 0.10769128625929614, 0.10374386641616549, 0.0916652344410777, 0.07958660246598985, 0.11950990854411785, 0.13158854051920571, 0.099796446573035186, 0.10296383734536738, 0.10740763932446029], '214': [0.12627765123670265, 0.31446760951342106, 0.089421699468973492, 0.10772125740242791, 0.083236234857548552, 0.11724558872451812, 0.071828440262775239, 0.097512030344816494, 0.054387314268601793, 0.083000801948463154, 0.028458930171942256, 0.10821352621233365, 0.033109743383802417, 0.09036343110531507, 0.093231431997809602, 0.097255194443996038], '257': [0.014856241243968688, 0.046945722330941131, 0.010520233206322257, 0.012673129183202533, 0.0097925291860668125, 0.013793642293976364, 0.0084504314601286518, 0.011472039848732461, 0.011051532681318412, 0.0097648311091713038, 0.0084781295370241899, 0.012731043343984024, 0.014017744916131154, 0.010631025513904347, 0.010968438450631807, 0.011441823764846403], '415': [0.050225214764677686, 0.036530970201609642, 0.035566262252003926, 0.042844662018749632, 0.033106078003361288, 0.046632834996763448, 0.028568783178009906, 0.038784081096249381, 0.037362452135961025, 0.033012437772444059, 0.028662423408927069, 0.043040455228849209, 0.047390469592366265, 0.035940823175672799, 0.037081531443209532, 0.038681928117066992], '710': [0.089674027645291116, 0.28336992735911998, 0.063501370763055329, 0.076496505277754243, 0.059108863307209714, 0.083260054820492299, 0.051007802843660542, 0.069246588127448522, 0.066708357175454674, 0.058941674442108294, 0.051174991708761851, 0.076846081995693538, 0.050483450975609093, 0.064170126223460897, 0.06620679058015054, 0.06906420027461066], '887': [0.057053046346716159, 0.18028762645562316, 0.040401292819759363, 0.048669149536105509, 0.037606660549555769, 0.01551759777805072, 0.032452546362640604, 0.044056555789091338, 0.042441664477243589, 0.0375002904631467, 0.032558916449049735, 0.048891559716779172, 0.053832933730876102, 0.040826773165395923, 0.042122554218016202, 0.043940515694826814], '1010': [0.075382945098012438, 0.22746625088558872, 0.023886087322913935, 0.064305485199711271, 0.049688859912910249, 0.069991148007951184, 0.042878841313377922, 0.058210965740092289, 0.056077245090707849, 0.049548315438998652, 0.043019385787289428, 0.064599350917890014, 0.071128280569599203, 0.053943524441323464, 0.055655611668973239, 0.058057644495825199]}
rona.pop_ronas = defaultdict(list)
for k,v in rona_dict.items():
    rona.pop_ronas[k] = v
rona.corr_coef ={'109': 0.0006640909658998809, '145': 0.14430216359296372, '214': 0.10406403494450837, '257': 0.0012449897480285869, '415': 0.014196158980969362, '710': 0.055988694433971149, '887': 0.024541999123225522, '1010': 0.031127284539578529}
rona.avg_ronas = [0.069916590853416033, 0.33042827432762917, 0.078081886442357085, 0.097001282569124797, 0.074952908386911654, 0.08208789223743565, 0.064680370415653249, 0.087808035641750992, 0.073646989317191325, 0.074740904789005747, 0.05282815857307914, 0.097444562819291675, 0.07840782467814407, 0.081365771844823354, 0.083953424770734683, 0.087576758989489953]
rona.stderr_ronas = [0.013313151175645535, 0.049792720537769092, 0.011485830558008609, 0.013381880064626782, 0.010340181118882092, 0.012982193864458787, 0.0089230259282510414, 0.012113619227983244, 0.01029680158551243, 0.010310934013634544, 0.0079085804585694048, 0.013443033102871656, 0.01276549989475941, 0.011404533167324531, 0.011581853678027876, 0.012081713294985915]
ronas['11'] = rona

rona = pr.RonaClass("12")
rona_dict = {'649': [0.086850728432886104, 0.080731124560793566, 0.064680192750292742, 0.076100475402105461, 0.059230618499232099, 0.068328131798133768, 0.048807935505400434, 0.072467425901398486, 0.06881948685355728, 0.06386126765792019, 0.050624460255753921, 0.058164563645681781, 0.084215278590160134, 0.076264260420579988, 0.065514007389799275, 0.070814686169519414], '707': [0.013144357178726815, 0.012218190403404194, 0.0097889743844315116, 0.011517368342271985, 0.008964212730494624, 0.010341068934198124, 0.0073867997311617374, 0.010967527239647418, 0.010415432689880877, 0.0096650347916268503, 0.0076617202824740211, 0.011868906096409067, 0.0086073572837947112, 0.01154215626083294, 0.0099151674243781809, 0.010717394606896052], '784': [0.023412187537834438, 0.10163030427622605, 0.081424205417913259, 0.095800900987788859, 0.074563878718337695, 0.086016500612984326, 0.061443035303848932, 0.0047645632706270645, 0.081945602066328824, 0.080393282006774883, 0.063729810870374076, 0.093075869060004354, 0.10601641478906937, 0.09600708567001659, 0.082473872891072414, 0.089146758970440956]}
rona.pop_ronas = defaultdict(list)
for k,v in rona_dict.items():
    rona.pop_ronas[k] = v
rona.corr_coef = {'649': 0.016349693873427815, '707': 0.00036288134317020955, '784': 0.043514409885779509}
rona.avg_ronas = [0.040571849732149917, 0.095418119191833364, 0.076447124634696412, 0.089945040057074904, 0.070006137614369746, 0.08075871430677295, 0.057687309979865299, 0.023181092279660542, 0.077951297370389791, 0.075479216749128192, 0.059834305653307468, 0.083109279382294843, 0.09951119404950319, 0.090138621634188593, 0.07743263084545679, 0.083697634613861913]
rona.stderr_ronas = [0.018819322196863317, 0.022048199697093925, 0.017664584928841015, 0.020783539035751947, 0.016176270452792248, 0.018660861012534825, 0.013329767356524136, 0.017642952538880076, 0.017950439563746097, 0.017440931114134219, 0.013825872181873717, 0.019203257813331393, 0.024098848741442403, 0.020828269798693309, 0.017892305176542465, 0.019339955322644532]
ronas['12'] = rona

rona = pr.RonaClass("14")
rona_dict = {'250': [0.024094829252647242, 0.0080535780488881388, 0.00036906740649573545, 0.0092266851623922785, 0.027535064720339297, 0.0066629847851275648, 0.00036906740649569203, 0.0014630886471793769, 0.01654871888769073, 0.0068804709353839323, 0.004830828731452518, 0.018163388791109365, 0.0013905932637605517, 0.0016080794140169408, 0.023066712905980696, 0.0013905932637605517], '278': [0.0083707381067368858, 0.0027978779995712125, 0.00012821699507037482, 0.0032054248767591949, 0.0095659036679285273, 0.0023147746788596672, 0.00012821699507037482, 0.00050828880188611369, 0.0057491584753874029, 0.0023903311223832922, 0.0016782688819032136, 0.0063101078288202578, 0.00048310332071156324, 0.0005586597642352147, 0.0080135621918979976, 0.00048310332071158085], '349': [0.030083050613182703, 0.01005511155615673, 0.00046079070961111329, 0.011519767740277832, 0.034378278299200551, 0.0083189179895863264, 0.00046079070961111329, 0.001826706027386894, 0.020661526282741132, 0.0085904553720357307, 0.0027722095426111044, 0.02267748563728977, 0.0017361935665704713, 0.0020077309490198411, 0.028799419350694581, 0.0017361935665704713], '421': [0.11892109729753635, 0.039748791273957675, 0.0018215485362861219, 0.045538713407152855, 0.056334051677992228, 0.032885456610451169, 0.0018215485362861219, 0.0072211388402771189, 0.081676935260972056, 0.033958869140762564, 0.023842769233887891, 0.089646210107223734, 0.0068633346635065757, 0.0079367471938180424, 0.11384678351788213, 0.0068633346635066416], '829': [0.054535665742069542, 0.018228277772650153, 0.0008353384249332285, 0.020883460623330775, 0.062322213203054304, 0.015080841921562444, 0.0008353384249332285, 0.0033115201845567216, 0.037455978303702592, 0.015573094921969528, 0.010933983312072472, 0.041110583912785416, 0.0031474358510877082, 0.0036396888514948359, 0.052208651558326963, 0.0031474358510877082]}
rona.pop_ronas = defaultdict(list)
for k,v in rona_dict.items():
    rona.pop_ronas[k] = v
rona.corr_coef = {'250': 0.0040724658723727027, '278': 0.00054093126158548193, '349': 0.0064761181412646201, '421': 0.1676523858378404, '829': 0.028274333835238769}
rona.avg_ronas = [0.10519387557463623, 0.035160534997867976, 0.0016112847462198174, 0.040282118655495261, 0.055776326583905605, 0.02908944425764699, 0.0016112847462198163, 0.0063875931010856932, 0.072248857102820474, 0.030038951340240753, 0.020988608029702958, 0.079298227867532073, 0.0060710907402210454, 0.0070205978228148717, 0.10070529663873815, 0.0060710907402210983]
rona.stderr_ronas = [0.017357739754244265, 0.0058017390535247491, 0.00026587347544794097, 0.0066468368861985682, 0.0086228380619286314, 0.0047999657799619802, 0.0002658734754479433, 0.0010539984205257748, 0.011921576729460438, 0.0049566412208509351, 0.0036531944886092765, 0.013084773184545175, 0.0010017732735627778, 0.0011584487144517435, 0.016617092215496416, 0.0010017732735627871]
ronas['14'] = rona

rona = pr.RonaClass("15")
rona_dict = {'63': [0.0041548828836814834, 0.028923691147344867, 0.0049573280758087529, 0.0051534813449954668, 0.0, 0.038838347298962475, 0.0011947517305006977, 0.012286327497238353, 0.005349634614182113, 0.0009985984613139836, 0.0019793648072474017, 0.0001961532691867142, 0.0037625763453081229, 0.011894020958864984, 0.0001961532691867142, 0.0073289994214295997], '121': [0.0064442414620758228, 0.044860771036424676, 0.0076888374526054692, 0.0024476349908443538, 0.0, 0.060238445941635611, 0.0018530651414552621, 0.019056147499443035, 0.0082973066035310853, 0.0015488305659924679, 0.0030700034433064939, 0.0003042345754628079, 0.0058357723111501798, 0.018447678348517418, 0.0003042345754628079, 0.011367310046837551], '128': [0.004270226164716436, 0.029726638794721393, 0.0050949479561853035, 0.0052965466163221306, 0.0, 0.039916534707092111, 0.0012279191117424892, 0.012627406984934081, 0.0054981452764589689, 0.0010263204516056837, 0.0020343137522898205, 0.00020159866013683841, 0.003867028844442847, 0.012224209664660427, 0.00020159866013681638, 0.0075324590287487786], '130': [0.018687379720911685, 0.13008982792840659, 0.022296530310787308, 0.023178767121645769, 0.0, 0.0095787024816304939, 0.0053736242115926484, 0.017000520619699467, 0.024061003932504297, 0.0044913874007341528, 0.0089025714550265943, 0.00088223681085849493, 0.016922906099194692, 0.053495632076601227, 0.00088223681085849493, 0.032963575387530926], '198': [0.0057012573938117449, 0.039688581514002827, 0.0068023586072088671, 0.0070715166815948213, 0.0, 0.053293298728420604, 0.0016394173621690632, 0.0168590830229026, 0.0073406747559807556, 0.0013702592877830764, 0.0027160496597128953, 0.0002691580743859866, 0.0051629412450398243, 0.01583812468218869, 0.0002691580743859866, 0.010056724415693765], '351': [0.0049797404699712198, 0.034665832799541885, 0.0059414929212531558, 0.0061765879648999333, 0.0, 0.028778903072305961, 0.0014319425385753899, 0.014725498642962012, 0.0064116830085465598, 0.0011968474949286881, 0.0023723227131622468, 0.00023509504364672672, 0.0045095503826777664, 0.014255308555668584, 0.0002350950436467142, 0.0087840057217088569], '398': [0.0038362676770137554, 0.026705691725821105, 0.0045771777433897222, 0.0047582890929483987, 0.0, 0.035860047212600735, 0.0011031327654932273, 0.011344156349624391, 0.0049394004425069825, 0.00092202141593462808, 0.0018275781637275934, 0.00018111134955858379, 0.0034740449778965878, 0.010981933650507193, 0.00018111134955859929, 0.0067669786062345763], '438': [0.004821987652786127, 0.019876817610221306, 0.0057532728217791554, 0.0059809203075329893, 0.0, 0.029567370645590094, 0.0013865801405007266, 0.014259010698582073, 0.0062085677932868389, 0.0011589326547468775, 0.002297170083516124, 0.00022764748575384932, 0.0043666926812784062, 0.013803715727074374, 0.00022764748575381972, 0.0085057378768029178], '526': [0.00090930830604254997, 0.0063300346454979719, 0.0010849257900422003, 0.0011278545083532093, 0.0, 0.0084998862255823548, 0.00026147492062167718, 0.0026888988105721674, 0.0011707832266642534, 0.0002185462023106681, 0.0004331897938657661, 4.2928718311022215e-05, 0.00082345086942052308, 0.002603041373950149, 4.2928718311026592e-05, 0.001603973020530002], '548': [0.0020518720143468442, 0.010509210891373473, 0.0024481563089631736, 0.0025450258032027216, 0.0, 0.019180159859430893, 0.00059002328309545437, 0.0060675528664590915, 0.00264189529744227, 0.00049315378885593454, 0.00097750126005364786, 9.6869494239548387e-05, 0.0018581330258677332, 0.0058738138779799659, 9.6869494239548387e-05, 0.0036193965574959465], '610': [0.010028705106904252, 0.069813560872956329, 0.011965579483774259, 0.012439037664786918, 0.0, 0.093744719840504878, 0.0028837907388952343, 0.02965569879251968, 0.012912495845799567, 0.0024103325578825902, 0.0047776234629458387, 0.00047345818101265957, 0.0090817887448789939, 0.028708782430494392, 0.00047345818101262899, 0.017690119308745419], '632': [0.011795739709021936, 0.082114548532332896, 0.014073886863124859, 0.014630767278572267, 0.0, 0.11026232225858267, 0.0033919079849977227, 0.034880964203931809, 0.015187647694019625, 0.0028350275695503326, 0.0056194296467872631, 0.00055688041544738347, 0.010681978878127116, 0.033767203373037048, 0.00055688041544738997, 0.020807077340806952], '769': [0.019041403888345056, 0.13255432234719178, 0.022718928244463216, 0.023617878642625462, 0.0, 0.17799217883611829, 0.0054754251524425776, 0.056306984030342261, 0.024516829040787634, 0.0045764747542803462, 0.0090712267450914277, 0.00089895039816221623, 0.017243503092020655, 0.054509083234017847, 0.00089895039816220127, 0.033588055785879062], '788': [0.010184919771864401, 0.070901029484824407, 0.012151964362997045, 0.012632797485273874, 0.0, 0.095204958210818494, 0.0029287108356863029, 0.030117638295341573, 0.013113630607550754, 0.0024478777134094858, 0.0048520433247937729, 0.00048083312227686751, 0.0092232535273106906, 0.029155972050787848, 0.00048083312227686751, 0.017965673932344526], '897': [0.0071110449064785532, 0.049502638791022499, 0.0084844226781160981, 0.0088201372445163382, 0.0, 0.066471484147254609, 0.0020448069044380433, 0.021027939659071876, 0.009155851810916606, 0.0017090923380377791, 0.0033876651700391496, 0.0003357145664002741, 0.0064396157736780254, 0.020356510526271288, 0.0003357145664002741, 0.012543516980955764], '938': [0.0068591233483873346, 0.047748918760018293, 0.0081838467418526833, 0.0085076680158108816, 0.0, 0.033426205119968494, 0.0019723659413817644, 0.020282987068836401, 0.0088314892897691285, 0.0016485446674235941, 0.0032676510372145677, 0.00032382127395819935, 0.0062114808004709301, 0.019635344520919969, 0.00032382127395819935, 0.012099140326983672], '948': [0.015863629990114328, 0.086408060633542103, 0.01892742118992178, 0.019676347927652518, 0.0, 0.14828749407068251, 0.0045616446752688939, 0.046910047481496887, 0.02042527466538329, 0.0038127179375382235, 0.0075573516261918132, 0.00074218253240479579, 0.014365776514652904, 0.045412194006035474, 0.00074892673773073839, 0.027982626291575104], '1000': [0.00072496317100067837, 0.0050467393277390162, 0.00086497751733137604, 0.00089920324643437053, 0.0, 0.0067766943624017126, 0.00020846580453668675, 0.0021437752138176273, 0.00093342897553745359, 0.00017424007543364797, 0.00034536872094884189, 3.4225729103038786e-05, 0.00065651171279464506, 0.0020753237556115495, 3.4225729103038786e-05, 0.0012787976964862954], '1161': [0.003529009310349059, 0.024566751508094911, 0.0042105776320902656, 0.0043771832218492618, 0.0, 0.032987906772275442, 0.0010147795012591557, 0.010435568303993406, 0.0045437888116081886, 0.00084817391150020238, 0.0016812018602950531, 0.00016660558975895322, 0.0031957981308310683, 0.010102357124475537, 0.00016660558975895322, 0.0062249906719032255]}
rona.pop_ronas = defaultdict(list)
for k,v in rona_dict.items():
    rona.pop_ronas[k] = v
rona.corr_coef = {'63': 0.0077456870585954412, '121': 0.039301225034401907, '128': 0.016111926538904166, '130': 0.18481379924616759, '198': 0.023750233063372327, '351': 0.017735489340372099, '398': 0.011325573184287981, '438': 0.018683796231953969, '526': 0.00049854828620604728, '548': 0.0031221991840612805, '610': 0.078319942162650966, '632': 0.11355218364094871, '769': 0.22867817097379825, '788': 0.083453021616355649, '897': 0.04690162704365064, '938': 0.038263261893703132, '948': 0.12921058644023001, '1000': 0.00031920701110584829, '1161': 0.0052277858268105553}
rona.avg_ronas = [0.013529574810934185, 0.090964013692765217, 0.016142582821629635, 0.0165731619528456, 0.0, 0.095626902254738605, 0.003890478593702105, 0.033254662531292369, 0.017420053404636298, 0.00325174330219878, 0.0064454197597154329, 0.00063790299842444922, 0.012252104227927531, 0.038719637257432278, 0.00063873529150333078, 0.023865473164351742]
rona.stderr_ronas = [0.0012326560237869524, 0.0083588763235082613, 0.0014707226378230585, 0.0015670042881442531, 0.0, 0.010661619342990508, 0.00035445473645375874, 0.0031727094664367557, 0.0015871107602407116, 0.00029626067524493279, 0.00058723098128906303, 5.8066989771126626e-05, 0.0011162679013693004, 0.0035306274108324173, 5.8194061208826052e-05, 0.0021743417415297753]
ronas['15'] = rona

rona = pr.RonaClass("16")
rona_dict = {'589': [0.019747076205946928, 0.051413558770438496, 0.086015417527705862, 0.035580317488192736, 0.00097845873092532458, 0.099802790554380544, 0.08992925245140708, 0.053788472527463597, 0.049456641308587894, 0.042518479398390312, 0.097845873092530025, 0.013876323820395157, 0.076141879424732495, 0.09882433182345525, 0.0, 0.022527513945124502]}
rona.pop_ronas = defaultdict(list)
for k,v in rona_dict.items():
    rona.pop_ronas[k] = v
rona.corr_coef = {'589': 0.17658228323645278}
rona.avg_ronas = [0.019747076205946928, 0.051413558770438496, 0.086015417527705862, 0.035580317488192736, 0.00097845873092532458, 0.099802790554380544, 0.08992925245140708, 0.053788472527463597, 0.049456641308587894, 0.042518479398390312, 0.097845873092530025, 0.013876323820395157, 0.076141879424732495, 0.09882433182345525, 0.0, 0.022527513945124502]
rona.stderr_ronas = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
ronas['16'] = rona

for r in ronas.values():
    r.pop_names = ['Algeria', 'Catalonia', 'Corsica', 'Haza_de_Lino', 'Kenitra', 'Landes', 'Monchique', 'Puglia', 'Sardinia', 'Sicilia', 'Sintra', 'Taza', 'Toledo', 'Tuscany', 'Tunisia', 'Var']

# Test functions

def test_basic_stats():
    """
    Test the function basic_stats of pyRona.py.
    """

    test_rona = pr.RonaClass('5')
    test_rona.pop_ronas = ronas['5'].pop_ronas
    test_rona.corr_coef = ronas['5'].corr_coef

    test_rona.basic_stats(True)

    assert test_rona.avg_ronas == ronas['5'].avg_ronas
    assert test_rona.stderr_ronas == ronas['5'].stderr_ronas

def test_count_markers():
    """
    Test the function count_markers of pyRona.py.
    """

    test_nr = ronas['5'].count_markers()
    control_nr = 4

    assert test_nr == control_nr

def test_calculate_rona():
    """
    Test the function calculate_rona of pyRona.py.
    """

    covar = "558"
    test_rona = pr.RonaClass('5')
    present_cov = np.array([114, 71, 59, 117, 107, 86, 93, 87, 80, 76, 71, 122, 118, 88, 98, 83,])
    future_cov = np.array([119.67, 72.78, 59.22, 120.11, 111.89, 91.22, 94.78, 88, 80.67, 76.89, 72.44, 128.67, 127.67, 91.11, 103.89, 83.78])
    al_freq = np.array([0.1957648, -0.49158111, 0.3691684, 0.27138479, -0.00115721, 0.29038402, -0.31815359, 0.23805522, 0.15150419, -0.31698508, 0.4346372, 0.13334157, -0.20163875, 0.8946341, -0.38784942, -0.55615943])
    plot = True
    outlier = 0
    rtype = "absdiff"

    pr.calculate_rona(covar, test_rona, present_cov, future_cov, al_freq, plot, outlier, rtype)

    control_pop_rona_dict = {'558': [0.0014018084856003402, 0.00044007391611439851, 5.4391158171442511e-05, 0.00076889319051446367, 0.0012089671066288572, 0.0012905538438860258, 0.00044007391611439851, 0.00024723253714292048, 0.00016564579988575674, 0.00022003695805716098, 0.0003560148534858055, 0.001649041022743251, 0.0023907386341719839, 0.00076889319051452103, 0.0014561996437717636, 0.000192841378971478]}
    control_pop_rona = defaultdict(list)
    for k,v in control_pop_rona_dict.items():
        control_pop_rona[k] = v

    assert test_rona.pop_ronas == control_pop_rona

def test_results_summary():
    """
    Test the function results_summary of pyRona.py.
    """

    top_ronas = [ronas['15'], ronas['11'], ronas['14']]

    test_results_summary = pr.results_summary(top_ronas, True)

    with open("tests/data/jar/pyRona.results_summary.pickle","rb") as f:
            control_results_summary = pickle.load(f)

    assert test_results_summary == control_results_summary

def test_ronas_filterer():
    """
    Test the function ronas_filterer of pyRona.py.
    """

    test_ronas_filtered = pr.ronas_filterer(ronas, True, 3)

    assert test_ronas_filtered[0] == ronas['15']
    assert test_ronas_filtered[1] == ronas['11']
    assert test_ronas_filtered[2] == ronas['14']

def test_argument_parser():
    """
    Test the function argument_parser of pyRona.py.
    """

    args = ['-pc', 'tests/data/ENVFILE', '-fc', 'tests/data/ENVFILE_rpc85', '-pop', 'tests/data/popnames_single_GEO.txt', '-beta', 'tests/data/Qsuber_GBS_mcmc_aux_summary_betai.out', '-pij', 'tests/data/Qsuber_GBS_mcmc_aux_summary_pij.out', '-out', '/home/baptista/Music/LOL', '-bf', '20', '-outliers', '0']

    test_arguments = pr.argument_parser(args)

    control_arguments = "Namespace(bayes_factor=20.0, baypass_pij_file='tests/data/Qsuber_GBS_mcmc_aux_summary_pij.out', baypass_summary_betai_file='tests/data/Qsuber_GBS_mcmc_aux_summary_betai.out', future_covars_file='tests/data/ENVFILE_rpc85', immutables=['1', '2', '3'], num_covars=3, outfile='/home/baptista/Music/LOL', outliers=0, plots=True, popnames_file='tests/data/popnames_single_GEO.txt', present_covars_file='tests/data/ENVFILE', rtype='absdiff', use_weights=True)"

    assert str(test_arguments) == control_arguments
