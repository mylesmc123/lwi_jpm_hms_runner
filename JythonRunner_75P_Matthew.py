'''
Created on Oct 9, 2020

@author: MYMCMANUS-LOCAL
'''
# Instructions for running the HMS Jython Interpretor via the Windows Command Prompt here: https://www.hec.usace.army.mil/confluence/hmsdocs/hmsguides/running-hec-hms-with-jython  
# Example: cd /d C:/Programs/HEC-HMS-4.4
# hec-hms.cmd -script C:/jy/Runner.py

from hms.model import Project
from hms import Hms


# myProject = Project.open(r"Z:\Amite\HEC_HMS_RE-Calibration\HMS_Model_AORC_TS_Matthew\Amite_Final_HMS_Model.hms")

myProject = Project.open("Z:\Amite\HMS_9_simulations_AORC_bins\Matthew\HMS_Models_Hurricanes_AORC_75Percentiles\Amite_Final_HMS_Model.hms")

runList = ['TS_Matthew_75P_JPM_Sim1', 'TS_Matthew_75P_JPM_Sim10', 'TS_Matthew_75P_JPM_Sim100', 'TS_Matthew_75P_JPM_Sim101', 'TS_Matthew_75P_JPM_Sim102', 'TS_Matthew_75P_JPM_Sim103', 'TS_Matthew_75P_JPM_Sim104', 'TS_Matthew_75P_JPM_Sim105', 'TS_Matthew_75P_JPM_Sim106', 'TS_Matthew_75P_JPM_Sim107', 'TS_Matthew_75P_JPM_Sim108', 'TS_Matthew_75P_JPM_Sim109', 'TS_Matthew_75P_JPM_Sim11', 'TS_Matthew_75P_JPM_Sim110', 'TS_Matthew_75P_JPM_Sim111', 'TS_Matthew_75P_JPM_Sim112', 'TS_Matthew_75P_JPM_Sim113', 'TS_Matthew_75P_JPM_Sim114', 'TS_Matthew_75P_JPM_Sim115', 'TS_Matthew_75P_JPM_Sim116', 'TS_Matthew_75P_JPM_Sim117', 'TS_Matthew_75P_JPM_Sim118', 'TS_Matthew_75P_JPM_Sim119', 'TS_Matthew_75P_JPM_Sim12', 'TS_Matthew_75P_JPM_Sim120', 'TS_Matthew_75P_JPM_Sim121', 'TS_Matthew_75P_JPM_Sim122', 'TS_Matthew_75P_JPM_Sim123', 'TS_Matthew_75P_JPM_Sim124', 'TS_Matthew_75P_JPM_Sim125', 'TS_Matthew_75P_JPM_Sim126', 'TS_Matthew_75P_JPM_Sim127', 'TS_Matthew_75P_JPM_Sim128', 'TS_Matthew_75P_JPM_Sim129', 'TS_Matthew_75P_JPM_Sim13', 'TS_Matthew_75P_JPM_Sim130', 'TS_Matthew_75P_JPM_Sim131', 'TS_Matthew_75P_JPM_Sim132', 'TS_Matthew_75P_JPM_Sim133', 'TS_Matthew_75P_JPM_Sim134', 'TS_Matthew_75P_JPM_Sim135', 'TS_Matthew_75P_JPM_Sim136', 'TS_Matthew_75P_JPM_Sim137', 'TS_Matthew_75P_JPM_Sim138', 'TS_Matthew_75P_JPM_Sim139', 'TS_Matthew_75P_JPM_Sim14', 'TS_Matthew_75P_JPM_Sim140', 'TS_Matthew_75P_JPM_Sim141', 'TS_Matthew_75P_JPM_Sim142', 'TS_Matthew_75P_JPM_Sim143', 'TS_Matthew_75P_JPM_Sim144', 'TS_Matthew_75P_JPM_Sim145', 'TS_Matthew_75P_JPM_Sim146', 'TS_Matthew_75P_JPM_Sim147', 'TS_Matthew_75P_JPM_Sim148', 'TS_Matthew_75P_JPM_Sim149', 'TS_Matthew_75P_JPM_Sim15', 'TS_Matthew_75P_JPM_Sim150', 'TS_Matthew_75P_JPM_Sim151', 'TS_Matthew_75P_JPM_Sim152', 'TS_Matthew_75P_JPM_Sim153', 'TS_Matthew_75P_JPM_Sim154', 'TS_Matthew_75P_JPM_Sim155', 'TS_Matthew_75P_JPM_Sim156', 'TS_Matthew_75P_JPM_Sim157', 'TS_Matthew_75P_JPM_Sim158', 'TS_Matthew_75P_JPM_Sim159', 'TS_Matthew_75P_JPM_Sim16', 'TS_Matthew_75P_JPM_Sim160', 'TS_Matthew_75P_JPM_Sim161', 'TS_Matthew_75P_JPM_Sim162', 'TS_Matthew_75P_JPM_Sim163', 'TS_Matthew_75P_JPM_Sim164', 'TS_Matthew_75P_JPM_Sim165', 'TS_Matthew_75P_JPM_Sim166', 'TS_Matthew_75P_JPM_Sim167', 'TS_Matthew_75P_JPM_Sim168', 'TS_Matthew_75P_JPM_Sim169', 'TS_Matthew_75P_JPM_Sim17', 'TS_Matthew_75P_JPM_Sim170', 'TS_Matthew_75P_JPM_Sim171', 'TS_Matthew_75P_JPM_Sim172', 'TS_Matthew_75P_JPM_Sim173', 'TS_Matthew_75P_JPM_Sim174', 'TS_Matthew_75P_JPM_Sim175', 'TS_Matthew_75P_JPM_Sim176', 'TS_Matthew_75P_JPM_Sim177', 'TS_Matthew_75P_JPM_Sim178', 'TS_Matthew_75P_JPM_Sim179', 'TS_Matthew_75P_JPM_Sim18', 'TS_Matthew_75P_JPM_Sim180', 'TS_Matthew_75P_JPM_Sim181', 'TS_Matthew_75P_JPM_Sim182', 'TS_Matthew_75P_JPM_Sim183', 'TS_Matthew_75P_JPM_Sim184', 'TS_Matthew_75P_JPM_Sim185', 'TS_Matthew_75P_JPM_Sim186', 'TS_Matthew_75P_JPM_Sim187', 'TS_Matthew_75P_JPM_Sim188', 'TS_Matthew_75P_JPM_Sim189', 'TS_Matthew_75P_JPM_Sim19', 'TS_Matthew_75P_JPM_Sim190', 'TS_Matthew_75P_JPM_Sim191', 'TS_Matthew_75P_JPM_Sim192', 'TS_Matthew_75P_JPM_Sim193', 'TS_Matthew_75P_JPM_Sim194', 'TS_Matthew_75P_JPM_Sim195', 'TS_Matthew_75P_JPM_Sim196', 'TS_Matthew_75P_JPM_Sim197', 'TS_Matthew_75P_JPM_Sim198', 'TS_Matthew_75P_JPM_Sim199', 'TS_Matthew_75P_JPM_Sim2', 'TS_Matthew_75P_JPM_Sim20', 'TS_Matthew_75P_JPM_Sim200', 'TS_Matthew_75P_JPM_Sim201', 'TS_Matthew_75P_JPM_Sim202', 'TS_Matthew_75P_JPM_Sim203', 'TS_Matthew_75P_JPM_Sim204', 'TS_Matthew_75P_JPM_Sim205', 'TS_Matthew_75P_JPM_Sim206', 'TS_Matthew_75P_JPM_Sim207', 'TS_Matthew_75P_JPM_Sim208', 'TS_Matthew_75P_JPM_Sim209', 'TS_Matthew_75P_JPM_Sim21', 'TS_Matthew_75P_JPM_Sim210', 'TS_Matthew_75P_JPM_Sim211', 'TS_Matthew_75P_JPM_Sim212', 'TS_Matthew_75P_JPM_Sim213', 'TS_Matthew_75P_JPM_Sim214', 'TS_Matthew_75P_JPM_Sim215', 'TS_Matthew_75P_JPM_Sim216', 'TS_Matthew_75P_JPM_Sim217', 'TS_Matthew_75P_JPM_Sim218', 'TS_Matthew_75P_JPM_Sim219', 'TS_Matthew_75P_JPM_Sim22', 'TS_Matthew_75P_JPM_Sim220', 'TS_Matthew_75P_JPM_Sim221', 'TS_Matthew_75P_JPM_Sim222', 'TS_Matthew_75P_JPM_Sim223', 'TS_Matthew_75P_JPM_Sim224', 'TS_Matthew_75P_JPM_Sim225', 'TS_Matthew_75P_JPM_Sim226', 'TS_Matthew_75P_JPM_Sim227', 'TS_Matthew_75P_JPM_Sim228', 'TS_Matthew_75P_JPM_Sim229', 'TS_Matthew_75P_JPM_Sim23', 'TS_Matthew_75P_JPM_Sim230', 'TS_Matthew_75P_JPM_Sim231', 'TS_Matthew_75P_JPM_Sim232', 'TS_Matthew_75P_JPM_Sim233', 'TS_Matthew_75P_JPM_Sim234', 'TS_Matthew_75P_JPM_Sim235', 'TS_Matthew_75P_JPM_Sim236', 'TS_Matthew_75P_JPM_Sim237', 'TS_Matthew_75P_JPM_Sim238', 'TS_Matthew_75P_JPM_Sim239', 'TS_Matthew_75P_JPM_Sim24', 'TS_Matthew_75P_JPM_Sim240', 'TS_Matthew_75P_JPM_Sim241', 'TS_Matthew_75P_JPM_Sim242', 'TS_Matthew_75P_JPM_Sim243', 'TS_Matthew_75P_JPM_Sim244', 'TS_Matthew_75P_JPM_Sim245', 'TS_Matthew_75P_JPM_Sim246', 'TS_Matthew_75P_JPM_Sim247', 'TS_Matthew_75P_JPM_Sim248', 'TS_Matthew_75P_JPM_Sim249', 'TS_Matthew_75P_JPM_Sim25', 'TS_Matthew_75P_JPM_Sim250', 'TS_Matthew_75P_JPM_Sim251', 'TS_Matthew_75P_JPM_Sim252', 'TS_Matthew_75P_JPM_Sim253', 'TS_Matthew_75P_JPM_Sim254', 'TS_Matthew_75P_JPM_Sim255', 'TS_Matthew_75P_JPM_Sim256', 'TS_Matthew_75P_JPM_Sim257', 'TS_Matthew_75P_JPM_Sim258', 'TS_Matthew_75P_JPM_Sim259', 'TS_Matthew_75P_JPM_Sim26', 'TS_Matthew_75P_JPM_Sim260', 'TS_Matthew_75P_JPM_Sim261', 'TS_Matthew_75P_JPM_Sim262', 'TS_Matthew_75P_JPM_Sim263', 'TS_Matthew_75P_JPM_Sim264', 'TS_Matthew_75P_JPM_Sim265', 'TS_Matthew_75P_JPM_Sim266', 'TS_Matthew_75P_JPM_Sim267', 'TS_Matthew_75P_JPM_Sim268', 'TS_Matthew_75P_JPM_Sim269', 'TS_Matthew_75P_JPM_Sim27', 'TS_Matthew_75P_JPM_Sim270', 'TS_Matthew_75P_JPM_Sim271', 'TS_Matthew_75P_JPM_Sim272', 'TS_Matthew_75P_JPM_Sim273', 'TS_Matthew_75P_JPM_Sim274', 'TS_Matthew_75P_JPM_Sim275', 'TS_Matthew_75P_JPM_Sim276', 'TS_Matthew_75P_JPM_Sim277', 'TS_Matthew_75P_JPM_Sim278', 'TS_Matthew_75P_JPM_Sim279', 'TS_Matthew_75P_JPM_Sim28', 'TS_Matthew_75P_JPM_Sim280', 'TS_Matthew_75P_JPM_Sim281', 'TS_Matthew_75P_JPM_Sim282', 'TS_Matthew_75P_JPM_Sim283', 'TS_Matthew_75P_JPM_Sim284', 'TS_Matthew_75P_JPM_Sim285', 'TS_Matthew_75P_JPM_Sim286', 'TS_Matthew_75P_JPM_Sim287', 'TS_Matthew_75P_JPM_Sim288', 'TS_Matthew_75P_JPM_Sim289', 'TS_Matthew_75P_JPM_Sim29', 'TS_Matthew_75P_JPM_Sim290', 'TS_Matthew_75P_JPM_Sim291', 'TS_Matthew_75P_JPM_Sim292', 'TS_Matthew_75P_JPM_Sim293', 'TS_Matthew_75P_JPM_Sim294', 'TS_Matthew_75P_JPM_Sim295', 'TS_Matthew_75P_JPM_Sim296', 'TS_Matthew_75P_JPM_Sim297', 'TS_Matthew_75P_JPM_Sim298', 'TS_Matthew_75P_JPM_Sim299', 'TS_Matthew_75P_JPM_Sim3', 'TS_Matthew_75P_JPM_Sim30', 'TS_Matthew_75P_JPM_Sim300', 'TS_Matthew_75P_JPM_Sim301', 'TS_Matthew_75P_JPM_Sim302', 'TS_Matthew_75P_JPM_Sim303', 'TS_Matthew_75P_JPM_Sim304', 'TS_Matthew_75P_JPM_Sim305', 'TS_Matthew_75P_JPM_Sim306', 'TS_Matthew_75P_JPM_Sim307', 'TS_Matthew_75P_JPM_Sim308', 'TS_Matthew_75P_JPM_Sim309', 'TS_Matthew_75P_JPM_Sim31', 'TS_Matthew_75P_JPM_Sim310', 'TS_Matthew_75P_JPM_Sim311', 'TS_Matthew_75P_JPM_Sim312', 'TS_Matthew_75P_JPM_Sim313', 'TS_Matthew_75P_JPM_Sim314', 'TS_Matthew_75P_JPM_Sim315', 'TS_Matthew_75P_JPM_Sim316', 'TS_Matthew_75P_JPM_Sim317', 'TS_Matthew_75P_JPM_Sim318', 'TS_Matthew_75P_JPM_Sim319', 'TS_Matthew_75P_JPM_Sim32', 'TS_Matthew_75P_JPM_Sim320', 'TS_Matthew_75P_JPM_Sim321', 'TS_Matthew_75P_JPM_Sim322', 'TS_Matthew_75P_JPM_Sim323', 'TS_Matthew_75P_JPM_Sim324', 'TS_Matthew_75P_JPM_Sim325', 'TS_Matthew_75P_JPM_Sim326', 'TS_Matthew_75P_JPM_Sim327', 'TS_Matthew_75P_JPM_Sim328', 'TS_Matthew_75P_JPM_Sim329', 'TS_Matthew_75P_JPM_Sim33', 'TS_Matthew_75P_JPM_Sim330', 'TS_Matthew_75P_JPM_Sim331', 'TS_Matthew_75P_JPM_Sim332', 'TS_Matthew_75P_JPM_Sim333', 'TS_Matthew_75P_JPM_Sim334', 'TS_Matthew_75P_JPM_Sim335', 'TS_Matthew_75P_JPM_Sim336', 'TS_Matthew_75P_JPM_Sim337', 'TS_Matthew_75P_JPM_Sim338', 'TS_Matthew_75P_JPM_Sim339', 'TS_Matthew_75P_JPM_Sim34', 'TS_Matthew_75P_JPM_Sim340', 'TS_Matthew_75P_JPM_Sim341', 'TS_Matthew_75P_JPM_Sim342', 'TS_Matthew_75P_JPM_Sim343', 'TS_Matthew_75P_JPM_Sim344', 'TS_Matthew_75P_JPM_Sim345', 'TS_Matthew_75P_JPM_Sim346', 'TS_Matthew_75P_JPM_Sim347', 'TS_Matthew_75P_JPM_Sim348', 'TS_Matthew_75P_JPM_Sim349', 'TS_Matthew_75P_JPM_Sim35', 'TS_Matthew_75P_JPM_Sim350', 'TS_Matthew_75P_JPM_Sim351', 'TS_Matthew_75P_JPM_Sim352', 'TS_Matthew_75P_JPM_Sim353', 'TS_Matthew_75P_JPM_Sim354', 'TS_Matthew_75P_JPM_Sim355', 'TS_Matthew_75P_JPM_Sim356', 'TS_Matthew_75P_JPM_Sim357', 'TS_Matthew_75P_JPM_Sim358', 'TS_Matthew_75P_JPM_Sim359', 'TS_Matthew_75P_JPM_Sim36', 'TS_Matthew_75P_JPM_Sim360', 'TS_Matthew_75P_JPM_Sim361', 'TS_Matthew_75P_JPM_Sim362', 'TS_Matthew_75P_JPM_Sim363', 'TS_Matthew_75P_JPM_Sim364', 'TS_Matthew_75P_JPM_Sim365', 'TS_Matthew_75P_JPM_Sim366', 'TS_Matthew_75P_JPM_Sim367', 'TS_Matthew_75P_JPM_Sim368', 'TS_Matthew_75P_JPM_Sim369', 'TS_Matthew_75P_JPM_Sim37', 'TS_Matthew_75P_JPM_Sim370', 'TS_Matthew_75P_JPM_Sim371', 'TS_Matthew_75P_JPM_Sim372', 'TS_Matthew_75P_JPM_Sim373', 'TS_Matthew_75P_JPM_Sim374', 'TS_Matthew_75P_JPM_Sim375', 'TS_Matthew_75P_JPM_Sim376', 'TS_Matthew_75P_JPM_Sim377', 'TS_Matthew_75P_JPM_Sim378', 'TS_Matthew_75P_JPM_Sim379', 'TS_Matthew_75P_JPM_Sim38', 'TS_Matthew_75P_JPM_Sim380', 'TS_Matthew_75P_JPM_Sim381', 'TS_Matthew_75P_JPM_Sim382', 'TS_Matthew_75P_JPM_Sim383', 'TS_Matthew_75P_JPM_Sim384', 'TS_Matthew_75P_JPM_Sim385', 'TS_Matthew_75P_JPM_Sim386', 'TS_Matthew_75P_JPM_Sim387', 'TS_Matthew_75P_JPM_Sim388', 'TS_Matthew_75P_JPM_Sim389', 'TS_Matthew_75P_JPM_Sim39', 'TS_Matthew_75P_JPM_Sim390', 'TS_Matthew_75P_JPM_Sim391', 'TS_Matthew_75P_JPM_Sim392', 'TS_Matthew_75P_JPM_Sim393', 'TS_Matthew_75P_JPM_Sim394', 'TS_Matthew_75P_JPM_Sim395', 'TS_Matthew_75P_JPM_Sim396', 'TS_Matthew_75P_JPM_Sim397', 'TS_Matthew_75P_JPM_Sim398', 'TS_Matthew_75P_JPM_Sim399', 'TS_Matthew_75P_JPM_Sim4', 'TS_Matthew_75P_JPM_Sim40', 'TS_Matthew_75P_JPM_Sim400', 'TS_Matthew_75P_JPM_Sim401', 'TS_Matthew_75P_JPM_Sim402', 'TS_Matthew_75P_JPM_Sim403', 'TS_Matthew_75P_JPM_Sim404', 'TS_Matthew_75P_JPM_Sim405', 'TS_Matthew_75P_JPM_Sim406', 'TS_Matthew_75P_JPM_Sim407', 'TS_Matthew_75P_JPM_Sim408', 'TS_Matthew_75P_JPM_Sim409', 'TS_Matthew_75P_JPM_Sim41', 'TS_Matthew_75P_JPM_Sim410', 'TS_Matthew_75P_JPM_Sim411', 'TS_Matthew_75P_JPM_Sim412', 'TS_Matthew_75P_JPM_Sim413', 'TS_Matthew_75P_JPM_Sim414', 'TS_Matthew_75P_JPM_Sim415', 'TS_Matthew_75P_JPM_Sim416', 'TS_Matthew_75P_JPM_Sim417', 'TS_Matthew_75P_JPM_Sim418', 'TS_Matthew_75P_JPM_Sim419', 'TS_Matthew_75P_JPM_Sim42', 'TS_Matthew_75P_JPM_Sim420', 'TS_Matthew_75P_JPM_Sim421', 'TS_Matthew_75P_JPM_Sim422', 'TS_Matthew_75P_JPM_Sim423', 'TS_Matthew_75P_JPM_Sim424', 'TS_Matthew_75P_JPM_Sim425', 'TS_Matthew_75P_JPM_Sim426', 'TS_Matthew_75P_JPM_Sim427', 'TS_Matthew_75P_JPM_Sim428', 'TS_Matthew_75P_JPM_Sim429', 'TS_Matthew_75P_JPM_Sim43', 'TS_Matthew_75P_JPM_Sim430', 'TS_Matthew_75P_JPM_Sim431', 'TS_Matthew_75P_JPM_Sim432', 'TS_Matthew_75P_JPM_Sim433', 'TS_Matthew_75P_JPM_Sim434', 'TS_Matthew_75P_JPM_Sim435', 'TS_Matthew_75P_JPM_Sim436', 'TS_Matthew_75P_JPM_Sim437', 'TS_Matthew_75P_JPM_Sim438', 'TS_Matthew_75P_JPM_Sim439', 'TS_Matthew_75P_JPM_Sim44', 'TS_Matthew_75P_JPM_Sim440', 'TS_Matthew_75P_JPM_Sim441', 'TS_Matthew_75P_JPM_Sim442', 'TS_Matthew_75P_JPM_Sim443', 'TS_Matthew_75P_JPM_Sim444', 'TS_Matthew_75P_JPM_Sim445', 'TS_Matthew_75P_JPM_Sim446', 'TS_Matthew_75P_JPM_Sim447', 'TS_Matthew_75P_JPM_Sim448', 'TS_Matthew_75P_JPM_Sim449', 'TS_Matthew_75P_JPM_Sim45', 'TS_Matthew_75P_JPM_Sim450', 'TS_Matthew_75P_JPM_Sim451', 'TS_Matthew_75P_JPM_Sim452', 'TS_Matthew_75P_JPM_Sim453', 'TS_Matthew_75P_JPM_Sim454', 'TS_Matthew_75P_JPM_Sim455', 'TS_Matthew_75P_JPM_Sim456', 'TS_Matthew_75P_JPM_Sim457', 'TS_Matthew_75P_JPM_Sim458', 'TS_Matthew_75P_JPM_Sim459', 'TS_Matthew_75P_JPM_Sim46', 'TS_Matthew_75P_JPM_Sim460', 'TS_Matthew_75P_JPM_Sim461', 'TS_Matthew_75P_JPM_Sim462', 'TS_Matthew_75P_JPM_Sim463', 'TS_Matthew_75P_JPM_Sim464', 'TS_Matthew_75P_JPM_Sim465', 'TS_Matthew_75P_JPM_Sim466', 'TS_Matthew_75P_JPM_Sim467', 'TS_Matthew_75P_JPM_Sim468', 'TS_Matthew_75P_JPM_Sim469', 'TS_Matthew_75P_JPM_Sim47', 'TS_Matthew_75P_JPM_Sim470', 'TS_Matthew_75P_JPM_Sim471', 'TS_Matthew_75P_JPM_Sim472', 'TS_Matthew_75P_JPM_Sim473', 'TS_Matthew_75P_JPM_Sim474', 'TS_Matthew_75P_JPM_Sim475', 'TS_Matthew_75P_JPM_Sim476', 'TS_Matthew_75P_JPM_Sim477', 'TS_Matthew_75P_JPM_Sim478', 'TS_Matthew_75P_JPM_Sim479', 'TS_Matthew_75P_JPM_Sim48', 'TS_Matthew_75P_JPM_Sim480', 'TS_Matthew_75P_JPM_Sim481', 'TS_Matthew_75P_JPM_Sim482', 'TS_Matthew_75P_JPM_Sim483', 'TS_Matthew_75P_JPM_Sim484', 'TS_Matthew_75P_JPM_Sim485', 'TS_Matthew_75P_JPM_Sim486', 'TS_Matthew_75P_JPM_Sim487', 'TS_Matthew_75P_JPM_Sim488', 'TS_Matthew_75P_JPM_Sim489', 'TS_Matthew_75P_JPM_Sim49', 'TS_Matthew_75P_JPM_Sim490', 'TS_Matthew_75P_JPM_Sim491', 'TS_Matthew_75P_JPM_Sim492', 'TS_Matthew_75P_JPM_Sim493', 'TS_Matthew_75P_JPM_Sim494', 'TS_Matthew_75P_JPM_Sim495', 'TS_Matthew_75P_JPM_Sim496', 'TS_Matthew_75P_JPM_Sim497', 'TS_Matthew_75P_JPM_Sim498', 'TS_Matthew_75P_JPM_Sim499', 'TS_Matthew_75P_JPM_Sim5', 'TS_Matthew_75P_JPM_Sim50', 'TS_Matthew_75P_JPM_Sim500', 'TS_Matthew_75P_JPM_Sim51', 'TS_Matthew_75P_JPM_Sim52', 'TS_Matthew_75P_JPM_Sim53', 'TS_Matthew_75P_JPM_Sim54', 'TS_Matthew_75P_JPM_Sim55', 'TS_Matthew_75P_JPM_Sim56', 'TS_Matthew_75P_JPM_Sim57', 'TS_Matthew_75P_JPM_Sim58', 'TS_Matthew_75P_JPM_Sim59', 'TS_Matthew_75P_JPM_Sim6', 'TS_Matthew_75P_JPM_Sim60', 'TS_Matthew_75P_JPM_Sim61', 'TS_Matthew_75P_JPM_Sim62', 'TS_Matthew_75P_JPM_Sim63', 'TS_Matthew_75P_JPM_Sim64', 'TS_Matthew_75P_JPM_Sim65', 'TS_Matthew_75P_JPM_Sim66', 'TS_Matthew_75P_JPM_Sim67', 'TS_Matthew_75P_JPM_Sim68', 'TS_Matthew_75P_JPM_Sim69', 'TS_Matthew_75P_JPM_Sim7', 'TS_Matthew_75P_JPM_Sim70', 'TS_Matthew_75P_JPM_Sim71', 'TS_Matthew_75P_JPM_Sim72', 'TS_Matthew_75P_JPM_Sim73', 'TS_Matthew_75P_JPM_Sim74', 'TS_Matthew_75P_JPM_Sim75', 'TS_Matthew_75P_JPM_Sim76', 'TS_Matthew_75P_JPM_Sim77', 'TS_Matthew_75P_JPM_Sim78', 'TS_Matthew_75P_JPM_Sim79', 'TS_Matthew_75P_JPM_Sim8', 'TS_Matthew_75P_JPM_Sim80', 'TS_Matthew_75P_JPM_Sim81', 'TS_Matthew_75P_JPM_Sim82', 'TS_Matthew_75P_JPM_Sim83', 'TS_Matthew_75P_JPM_Sim84', 'TS_Matthew_75P_JPM_Sim85', 'TS_Matthew_75P_JPM_Sim86', 'TS_Matthew_75P_JPM_Sim87', 'TS_Matthew_75P_JPM_Sim88', 'TS_Matthew_75P_JPM_Sim89', 'TS_Matthew_75P_JPM_Sim9', 'TS_Matthew_75P_JPM_Sim90', 'TS_Matthew_75P_JPM_Sim91', 'TS_Matthew_75P_JPM_Sim92', 'TS_Matthew_75P_JPM_Sim93', 'TS_Matthew_75P_JPM_Sim94', 'TS_Matthew_75P_JPM_Sim95', 'TS_Matthew_75P_JPM_Sim96', 'TS_Matthew_75P_JPM_Sim97', 'TS_Matthew_75P_JPM_Sim98', 'TS_Matthew_75P_JPM_Sim99']
for run in runList:
    myProject.computeRun(run)

myProject.close()

Hms.shutdownEngine()