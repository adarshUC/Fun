__author__ = "Aadarsh"

from pyautogui import (sleep, write, press, FailSafeException)
import base64
import keyboard

# base64 ENCRYPTED LIST OF MSGs
j = ['TUFEQVJDSE9E', 'QkhPU0RJS0U=', 'TEFBQVdFRUUgS0UgQkFBQUFBTA==', 'TUFBQUFSIEtJIEpIQUFBQVQgS0UgQkJCQkJBQUFBQUxMTExM', 'TUFEUkNIT0QuLg==', 'VEVSSSBNQSBLSSBDSFVULi4=', 'TFdERSBLRSBCQUFBTExMLg==', 'TUFDSEFSIEtJIEpIQUFUIEtFIEJBQUFMTExM', 'VEVSSSBNQSBLSSBDSFVUIE0gRFUgVEFQQSBUQVA/', 'VEVSSSBNQSBLQSBCSE9TREFB', 'VEVSSSBCSE4gU0JTQkUgQkRJIFJBTkRJLg==', 'VEVSSSBNQSBPU1NFIEJBREkgUkFOREREREQ=', 'VEVSQSBCQUFQIENIS0FBQUE=', 'S0lUTkkgQ0hPRFUgVEVSSSBNQSBBQiBPUi4u', 'VEVSSSBNQSBDSE9EIERJIEhNIE5F', 'TUlHSFRZICEhICBCQUFQIEJPTFRF', 'VEVSSSBNQSBLRSBTVEggUkVFTFMgQk5FR0EgUk9BRCBQRUU=', 'VEVSSSBNQSBLSSBDSFVUIEVLIERBTSBUT1AgU0VYWQ==', 'TUFMVU0gTkEgUEhSIEtFU0UgTEVUQSBIVSBNIFRFUkkgTUEgS0kgQ0hVVCBUQVBBIFRBUFBQUFA=', 'TFVORCBLRSBDSE9ERSBUVSBLRVJFR0EgVFlQSU4=', 'U1BFRUQgUEtEIExXREVFRUU=', 'QkFBUCBLSSBTUEVFRCBNVENIIEtSUlI=', 'TFdERUVF', 'UEFQQSBLSSBTUEVFRCBNVENIIE5ISSBITyBSSEkgS1lB', 'QUxFIEFMRSBNRUxBIEJDSEFBQUE=', 'W0FEQVJTSF0odC5tZS9BQURBUlNIX0xFR0VORCkgVEVSQSBCQUFQICEh', 'Q0hVRCBHWUEgUEFQQSBTRUVF', 'S0lTQU4gS08gS0hPRE5BIE9S', 'U0FMRSBSQVBFS0wgS1JES0EgVEVSQQ==', 'SEFIQUhBQUFBQQ==', 'S0lEU1NTUw==', 'QkFDSEhFIFRFUkkgTUFBIEtJIENIVVRU', 'VEVSSSBCSEVOIEtJIENIVVRUIEJIT1NESVdBTEU=', 'VEVSSSBNQSBDSFVEIEdZSSBBQiBGUkFSIE1UIEhPTkE=', 'WUUgTEROR0UgQkFQUCBTRQ==', 'S0lEU1NTIEZSQVIgSEFIQUhI', 'QkhFTiBLRSBMV0RFIFNIUk0gS1I=', 'S0lUTkkgR0xJWUEgUERXRUdBIEFQTkkgTUEgS08=', 'U1VBUiBLRSBQSUxMRSBURVJJIE1BQUtPIFNBREFLIFBSIExJVEFLRSBDSE9EIERVTkdBID8/Pz8/Pw==', 'QUJFIFRFUkkgTUFBS0EgQkhPU0RBIE1BREVSQ0hPT0QgS1IgUElMTEUgUEFQQSBTRSBMQURFR0EgVFUgPz8/Pz8/', 'R0FMSSBHQUxJIE5FIFNIT1IgSEUgVEVSSSBNQUEgUkFOREkgQ0hPUiBIRSA/Pz8/Pz8=', 'QUJFIFRFUkkgQkVIRU4gS08gQ0hPRFUgUkFORElLRSBQSUxMRSBLVVRURSBLRSBDSE9ERSA/Pz8/Pz8=', 'VEVSSSBNQUFLTyBBSVNFIENIT0RBIEFJU0UgQ0hPREEgVEVSSSBNQUFBIEJFRCBQRUhJIE1VVEggRElBID8/Pz8/Pz8/', 'VEVSSSBCRUhFTiBLRSBCSE9TREUgTUUgQUFBRyBMQUdBRElBIE1FUkEgTU9UQSBMVU5EIERBTEtFID8/Pz8/Pz8/Pz8=', 'UkFORElLRSBCQUNISEUgVEVSSSBNQUFLTyBDSE9EVSBDSEFMIE5JS0FM', 'S0lUTkEgQ0hPRFUgVEVSSSBSQU5ESSBNQUFLSSBDSFVUSCBBQkIgQVBOSSBCRUhFTiBLTyBCSEVKID8/Pz8/Pw==', 'VEVSSSBCRUhFTiBLT1RPIENIT0QgQ0hPREtFIFBVUkEgRkFBRCBESUEgQ0hVVEggQUJCIFRFUkkgR0YgS08gQkhFSiA/Pz8/Pz8=', 'VEVSSSBHRiBLTyBFVE5BIENIT0RBIEJFSEVOIEtFIExPREUgVEVSSSBHRiBUTyBNRVJJIFJBTkRJIEJBTkdBWUkgQUJCIENIQUwgVEVSSSBNQUFLTyBDSE9EVEEgRklSU0UgPz8/Pz8/Pz8/Pz8/', 'SEFSSSBIQVJJIEdIQUFTIE1FIEpIT1BEQSBURVJJIE1BQUtBIEJIT1NEQSA/Pz8/Pz8/Pw==', 'Q0hBTCBURVJFIEJBQVAgS08gQkhFSiBURVJBIEJBU0tBIE5ISSBIRSBQQVBBIFNFIExBREVHQSBUVQ==', 'VEVSSSBCRUhFTiBLSSBDSFVUSCBNRSBCT01CIERBTEtFIFVEQSBEVU5HQSBNQUFLRSBMQVdERQ==', 'VEVSSSBNQUFLTyBUUkFJTiBNRSBMRUpBS0UgVE9QIEJFRCBQRSBMSVRBS0UgQ0hPRCBEVU5HQSBTVUFSIEtFIFBJTExFID8/Pz8/Pz8/', 'VEVSSSBNQUFBS0UgTlVERVMgR09PR0xFIFBFIFVQTE9BRCBLQVJEVU5HQSBCRUhFTiBLRSBMQUVXREUgPz8/Pw==', 'VEVSSSBNQUFBS0UgTlVERVMgR09PR0xFIFBFIFVQTE9BRCBLQVJEVU5HQSBCRUhFTiBLRSBMQUVXREUgPz8/Pw==', 'VEVSSSBCRUhFTiBLTyBDSE9EIENIT0RLRSBWSURFTyBCQU5BS0UgWE5YWC5DT00gUEUgTkVFTEFNIEtBUkRVTkdBIEtVVFRFIEtFIFBJTExFID8/Pz8=', 'VEVSSSBNQUFBS0kgQ0hVREFJIEtPIFBPUk5IVUIuQ09NIFBFIFVQTE9BRCBLQVJEVU5HQSBTVUFSIEtFIENIT0RFID8/Pz8/Pw==', 'QUJFIFRFUkkgQkVIRU4gS08gQ0hPRFUgUkFORElLRSBCQUNISEUgVEVSRUtPIENIQUtLTyBTRSBQSUxXQVZVTkdBIFJBTkRJS0UgQkFDSEhFID8/Pz8=', 'VEVSSSBNQUFLSSBDSFVUSCBGQUFES0UgUkFLRElBIE1BQUtFIExPREUgSkFBIEFCQiBTSUxXQUxFID8/Pz8=', 'VEVSSSBCRUhFTiBLSSBDSFVUSCBNRSBNRVJBIExVTkQgS0FBTEE=', 'VEVSSSBCRUhFTiBMRVRJIE1FUkkgTFVORCBCQURFIE1BU1RJIFNFIFRFUkkgQkVIRU4gS08gTUVORSBDSE9EIERBTEEgQk9IT1QgU0FTVEUgU0U=', 'QkVURSBUVSBCQUFQIFNFIExFR0EgUEFOR0EgVEVSSSBNQUFBIEtPIENIT0QgRFVOR0EgS0FSS0UgTkFOR0EgPz8/Pw==', 'SEFIQUhBSCBNRVJFIEJFVEUgQUdMSSBCQUFSIEFQTkkgTUFBS08gTEVLRSBBQVlBIE1BVEggS0FUIE9SIE1FUkUgTU9URSBMVU5EIFNFIENIVURXQVlBIE1BVEggS0FS', 'Q0hBTCBCRVRBIFRVSkhFIE1BQUYgS0lBID8/', 'QUJCIEFQTkkgR0YgS08gQkhFSg==', 'U0hBUkFNIEtBUiBURVJJIEJFSEVOIEtBIEJIT1NEQSBLSVROQSBHQUFMSUEgU1VOV0FZRUdBIEFQTkkgTUFBQSBCRUhFTiBLRSBVUEVS', 'QUJFIFJBTkRJS0UgQkFDSEhFIEFVS0FUIE5ISSBIRVRPIEFQTkkgUkFOREkgTUFBS08gTEVLRSBBQVlBIE1BVEggS0FSIEhBSEFIQUhB', 'S0lEWiBNQURBUkNIT0QgVEVSSSBNQUFLTyBDSE9EIENIT0RLRSBURVJSIExJWUUgQkhBSSBERURJWUE=', 'SlVOR0xFIE1FIE5BQ0hUQSBIRSBNT1JFIFRFUkkgTUFBS0kgQ0hVREFJIERFS0tFIFNBQiBCT0xURSBPTkNFIE1PUkUgT05DRSBNT1JFID8/Pz8/Pz8/', 'R0FMSSBHQUxJIE1FIFJFSFRBIEhFIFNBTkQgVEVSSSBNQUFLTyBDSE9EIERBTEEgT1IgQkFOQSBESUEgUkFORCA/Pz8/', 'U0FCIEJPTFRFIE1VSkhLTyBQQVBBIEtZT1VOS0kgTUVORSBCQU5BRElBIFRFUkkgTUFBS08gUFJFR05FTlQgPz8/Pw==', 'U1VBUiBLRSBQSUxMRSBURVJJIE1BQUtJIENIVVRIIE1FIFNVQVIgS0EgTE9VREEgT1IgVEVSSSBCRUhFTiBLSSBDSFVUSCBNRSBNRVJBIExPREE=', 'Pz8/Pz8/Pz8/Pz8/ID8/Pz8gPz8/Pz8/ID8/Pz8/PyA/Pz8/ID8/Pz8/Pz8/Pz8/PyA/Pz8/Pz8/Pz8/ID8/Pz8/Pz8/Pz8/PyA/Pz8/ID8/Pz8/Pz8/ID8/Pz8/Pz8/ID8/Pz8gPz8/Pz8/ID8/Pz8/PyA/Pz8/ID8/Pz8/Pz8/Pz8/Pz8/Pz8/PyA/Pz8/Pz8gPz8/Pz8/Pz8/Pz8/Li4uPz8/Pz8/', 'Q0hBTCBDSEFMIEFQTkkgTUFBS0kgQ0hVQ0hJWUEgRElLQQ==', 'SEFIQUhBSEEgQkFDSEhFIFRFUkkgTUFBQUtPIENIT0QgRElBIE5BTkdBIEtBUktF', 'VEVSSSBHRiBIRSBCQURJIFNFWFkgVVNLTyBQSUxBS0UgQ0hPT0RFTkdFIFBFUFNJ', 'MiBSVVBBWSBLSSBQRVBTSSBURVJJIE1VTU1ZIFNBQlNFIFNFWFkgPz8/Pw==', 'VEVSSSBNQUFLTyBDSEVFTVMgU0UgQ0hVRFdBVlVOR0EgTUFERVJDSE9PRCBLRSBQSUxMRSA/Pz8/', 'VEVSSSBCRUhFTiBLSSBDSFVUSCBNRSBNVVRIS0UgRkFSQVIgSE9KQVZVTkdBIEhVSSBIVUkgSFVJ', 'U1BFRUQgTEFBQSBURVJJIEJFSEVOIENIT0RVIFJBTkRJS0UgUElMTEUgPz8/Pz8/', 'QVJFIFJFIE1FUkUgQkVURSBLWU9VTiBTUEVFRCBQQUtBRCBOQSBQQUFBIFJBSEEgQVBORSBCQUFQIEtBIEhBSEFIPz8/Pw==', 'U1VOIFNVTiBTVUFSIEtFIFBJTExFIEpIQU5UTyBLRSBTT1VEQUdBUiBBUE5JIE1VTU1ZIEtJIE5VREVTIEJIRUo=', 'QUJFIFNVTiBMT0RFIFRFUkkgQkVIRU4gS0EgQkhPU0RBIEZBQUQgRFVOR0E=', 'VEVSSSBNQUFLTyBLSFVMRSBCQUpBUiBNRSBDSE9EIERBTEEgPz8/Pz8/', 'U0hSTSBLUg==', 'TUVSRSBMVU5EIEtFIEJBQUFBQUxMTExM', 'S0lUTkkgR0xJWUEgUERXWUdBIEFQTkkgTUEgQkhFTiBLTw==', 'Uk5ESSBLRSBMREtFRUVFRUVFRUU=', 'S0lEU1NTU1NTU1NTU1NT', 'QXBuaSBnYWFuZCBtZWluIG11dGhpIGRhYWw=', 'QXBuaSBsdW5kIGNob29z', 'QXBuaSBtYSBrbyBqYSBjaG9vcw==', 'QmhlbiBrZSBsYXVkZQ==', 'QmhlbiBrZSB0YWtrZQ==', 'QWJsYSBURVJBIEtIQU4gREFOIENIT0RORSBLSSBCQVJJSUk=', 'QkVURSBURVJJIE1BIFNCU0UgQkRJIFJBTkQ=', 'TFVORCBLRSBCQUFBTCBKSEFUIEtFIFBJU1NTVVVVVVVVVQ==', 'TFVORCBQRSBMVEtJVCBNQUFBTExMTCBLSSBCT05EIEggVFVVVQ==', 'S0FTSCBPUyBESU4gTVVUSCBNUktFIFNPSlRBIE0gVFVOIFBBSURBIE5BIEhPVEFB', 'R0xUSSBLUkRJIFRVSlcgUEFJREEgS1JLRQ==', 'U1BFRUQgUEtEREQ=', 'R2FhbmQgbWFpbiBMV0RBIERBTCBMRSBBUE5JIE1FUkFBQQ==', 'R2FhbmQgbWVpbiBiYW1idSBERURVTkdBQUFBQUE=', 'R0FORCBGVEkgS0UgQkFMS0tL', 'R290ZSBraXRuZSBiaGkgYmFkZSBobywgbHVuZCBrZSBuaWNoZSBoaSByZWh0ZSBoYWk=', 'SGF6YWFyIGx1bmQgdGVyaSBnYWFuZCBtYWlu', 'SmhhYW50IGtlIHBpc3N1LQ==', 'VEVSSSBNQSBLSSBLQUxJIENIVVQ=', 'S2hvdGV5IGtpIGF1bGFk', 'S3V0dGUga2EgYXdsYWQ=', 'S3V0dGUga2kgamF0', 'S3V0dGUga2UgdGF0dGU=', 'VEVUSSBNQSBLSS5DSFVUICwgdEVSSSBNQSBSTkRJSUlJSUlJSUlJSUlJSUlJSUlJSQ==', 'TGF2ZGUga2UgYmFs', 'bXVoIG1laSBsZWxl', 'THVuZCBLZSBQYXNpbmU=', 'TUVSRSBMV0RFIEtFIEJBQUFBQUxMTA==', 'SEFIQUhBQUFBQUE=', 'Q0hVRCBHWUFBQUFB', 'UmFuZGkga2hhbkUgS0kgVUxBRERE', 'U2FkaSBodWkgZ2FhbmQ=', 'VGVyaSBnYWFuZCBtYWluIGt1dGUga2EgbHVuZA==', 'VGVyaSBtYWEga2EgYmhvc2Rh', 'VGVyaSBtYWEga2kgY2h1dA==', 'VGVyZSBnYWFuZCBtZWluIGtlZWRlIHBhZGF5', 'VWxsdSBrZSBwYXRoZQ==', 'U1VOTiBNQURFUkNIT0Q=', 'VEVSSSBNQUEgS0EgQkhPU0RB', 'QkVIRU4gSyBMVU5E', 'VEVSSSBNQUEgS0EgQ0hVVCBLSSBDSFROSUlJSQ==', 'TUVSQSBMQVdEQSBMRUxFIFRVIEFHQVIgQ0hBSVlFIFRPSA==', 'R0FBTkRV', 'Q0hVVElZQQ==', 'VEVSSSBNQUEgS0kgQ0hVVCBQRSBKQ0IgQ0hBREhBQSBEVU5HQQ==', 'U0FNSkhBQSBMQVdERQ==', 'WUEgRFUgVEVSRSBHQUFORCBNRSBUQVBBQSBUQVA/Pw==', 'VEVSSSBCRUhFTiBNRVJBIFJPWiBMRVRJIEhBSQ==', 'VEVSSSBHRiBLIFNBQVRIIE1NUyBCQU5BQSBDSFVLQSBIVT8/Pz8/Pw==', 'VFUgQ0hVVElZQSBURVJBIEtIQU5EQUFOIENIVVRJWUE=', 'QVVSIEtJVE5BIEJPTFUgQkVZIE1BTk4gQkhBUiBHQVlBIE1FUkE/Pw==', 'VEVSSUlJSUlJIE1BQUFBIEtJIENIVVRUVCBNRSBBQkNEIExJS0ggRFVOR0EgTUFBIEtFIExPREU=', 'VEVSSSBNQUEgS08gTEVLQVIgTUFJIEZBUkFS', 'UkFOSURJSUk=', 'QkFDSEVF', 'Q0hPRFU=', 'UkFOREk=', 'UkFOREkgS0UgUElMTEU=', 'VEVSSUlJSUkgTUFBQSBLTyBCSEVKSko=', 'VEVSQUEgQkFBQUFQIEhV', 'dGVyaSBNQUEgS0kgQ0hVVCBNRSBIQUFUIERBQUxMS0UgQkhBQUcgSkFBTlVHQQ==', 'VGVyaSBtYWEgS08gU0FSQUsgUEUgTEVUQUEgRFVOR0E=', 'VEVSSSBNQUEgS08gR0IgUk9BRCBQRSBMRUpBS0UgQkVDSCBEVU5HQQ==', 'VGVyaSBtYWEgS0kgQ0hVVCBNRSBLQUFMSSBNSVRDSA==', 'VEVSSSBNQUEgU0FTVEkgUkFOREkgSEFJ', 'VEVSSSBNQUEgS0kgQ0hVVCBNRSBLQUJVVEFSIERBQUwgS0UgU09VUCBCQU5BVU5HQSBNQURBUkNIT0Q=', 'VEVSSSBNQUFBIFJBTkRJIEhBSQ==', 'VEVSSSBNQUFBIEtJIENIVVQgTUUgREVUT0wgREFBTCBEVU5HQSBNQURBUkNIT0Q=', 'VEVSSSBNQUEgS0FBQSBCSE9TREFB', 'VEVSSSBNQUEgS0kgQ0hVVCBNRSBMQVBUT1A=', 'VGVyaSBtYWEgUkFOREkgSEFJ', 'VEVSSSBNQUEgS08gQklTVEFSIFBFIExFVEFBS0UgQ0hPRFVOR0E=', 'VEVSSSBNQUEgS08gQU1FUklDQSBHSFVNQUFVTkdBIE1BREFSQ0hPRA==', 'VEVSSSBNQUEgS0kgQ0hVVCBNRSBOQUFSSVlBTCBQSE9SIERVTkdB', 'VEVSSSBNQUEgS0UgR0FORCBNRSBERVRPTCBEQUFMIERVTkdB', 'VEVSSSBNQUFBIEtPIEhPUkxJQ0tTIFBJTEFVTkdBIE1BREFSQ0hPRA==', 'VEVSSSBNQUEgS08gU0FSQUsgUEUgTEVUQUFBIERVTkdBQUE=', 'VEVSSSBNQUEgS0FBIEJIT1NEQQ==', 'TUVSQUFBIExVTkQgUEFLQUQgTEUgTUFEQVJDSE9E', 'Q0hVUCBURVJJIE1BQSBBS0FBIEJIT1NEQUE=', 'VEVSSUlJIE1BQSBDSFVGIEdFWUlJIEtZQUFBIExBV0RFRUU=', 'VEVSSUlJIE1BQSBLQUEgQkpTT0RBQUE=', 'TUFEQVJYSE9EREQ=', 'VEVSSVVVSSBNQUFBIEtBQSBCSFNPREFBQQ==', 'VEVSSUlJSUlJIEJFSEVOTk5OIEtPIENIT0RERFVVVVUgTUFEQVJYSE9ERERE', 'TklLQUwgTUFEQVJDSE9E', 'UkFOREkgS0UgQkFDSEU=', 'VEVSQSBNQUEgTUVSSSBGQU4=', 'VEVSSSBTRVhZIEJBSEVOIEtJIENIVVQgT1A=']
k = ['VFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRU', 'UlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJS', 'RUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRQ==', 'SUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSQ==', 'TU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTQ==', 'QUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUE=', 'S0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0s=', 'SUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUk=', 'Q0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0ND', 'SEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEg=', 'VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV', 'VFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRU', 'UlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUg==', 'QUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUE=', 'Tk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk4=', 'RERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERE', 'SUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSQ==', 'S0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSw==', 'RUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVF', 'Q0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQw==', 'SEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISEhISA==', 'T09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT08=', 'RERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERE', 'S0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSw==', 'UlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJS', 'Tk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk5OTk4=', 'RERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERE', 'SkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSkpKSko=', 'VFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVA==', 'VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVU=', 'TExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExMTExM', 'RERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERE', 'R0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR0c=', 'QUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFB', 'UFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQ', 'U1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NTU1NT', 'RUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUVFRUU=', 'QkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJCQkJC', 'Q0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0NDQ0M=', 'UlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJS', 'QU5ESUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJSUlJ', 'QUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFB']
l = ['VEVSSUlJSUlJ', 'TUFBQSBLSUlJSQ==', 'Q0hVVFQgTUFSVVVVVQ==', 'TUFERVJSQ0hPREQ=', 'QkVIRU5OIEtFRSBMT0RFRUU=', 'VEVSSUlJIE1BQUE=', 'S09PIEFJU0FBIENIT0RBQUE=', 'TUFERUVSQ0hPREQ=', 'S0FBTEFBUCBHWUlJ', 'VEVSSUkgTUFBQQ==', 'VEVSQUFB', 'S0hBTkRBQU5OIEtP', 'QU5EQVJSUlIgVEtL', 'Q0hPRCBEQUxBQUE=', 'VEVSSUlJSQ==', 'QkVIRU5OTg==', 'QUJISUkgTUVSRUU=', 'U0VFRUU=', 'Q0hVREQgUkhJIEhBSUlJ', 'TUFERVJSQ0hPRERE', 'VEVSSUlJ', 'TUFBQSBLSUlJ', 'Q0hVVFQgTUVF', 'SEFUSElJIEtBQQ==', 'TEFVREFB', 'R0hVU0FBIERJWUFB', 'TUFERUVSUkNIT0RERA==', 'UkFORElJ', 'S0FB', 'UElMTEFBQQ==', 'QkVIRU5DSE9EREQ=', 'VEVSSUlJ', 'QkVIRU5O', 'S0lJSQ==', 'Q0hVVFRU', 'TUVFRQ==', 'VE9XRVJSUg==', 'R0hVU0FBIERJWUFB', 'TUFERVJSUkNIT0RE', 'VEVSQUFB', 'QkFBQVA=', 'SFVJTk4=', 'QlNES0tLSw==', 'R0FOREQ=', 'TUFSUg==', 'TUFSUlI=', 'S0VFRQ==', 'WklOREFHSUlJSQ==', 'QU5ESEVSSUlJ', 'S0FSUlJS', 'RFVHQUFB', 'TUFERVJSUkNIT0RERA==', 'QkVIRU5OTg==', 'S0VFRQ==', 'TE9ERUVF', 'QUlTQUFB', 'Q0hPRFVHQUFB', 'QlNES0tL', 'UEhJUlJS', 'U0VFRQ==', 'S0lTSUlJ', 'U0VFRSBHQU5ERA==', 'TUFSQU5FRQ==', 'S0VF', 'TEFZQUtLSw==', 'TkFISUkgQkFDSEVHQUFB', 'QkFBQVBTRUVF', 'UEFOR0FB', 'TElZQSBIQUlJSQ==', 'QlNES0sgVFVVVQ==', 'QU5EQVJSUiBUQUs=', 'Q0hVREVHR0FBQQ==', 'VEVSSUlJ', 'TUFBQUE=', 'S0FBQSBSQVBFRQ==', 'S0FSUiBESVlBQQ==', 'TUFERVJSQ0hPRERE', 'QkVIRU5DSE9ERA==', 'VEVSQUFB', 'QVNMSUlJ', 'QkFBQVAgTUFJTk4=', 'SEkgSFVJTk5O', 'QlNES0s=', 'VEVSSSBNQUE=', 'S09PIEtPVEhFRQ==', 'UEUgQ0hPREFB', 'VEhBQSBHSE9ESUkgQkFOQUtFRQ==', 'SkFLRUVF', 'UFVDSEhIIEFQTkk=', 'QVBOSQ==', 'U0FNSkhBQSBMQVdERQ==', 'TUFBQSBTRUU=', 'VEVSSSBBU0xJSQ==', 'QkFBQVA=', 'TUFJTiBISSBIVUlOTg==', 'TUVSQUEgTkFKQVlBWg==', 'QkVUQSBIQUkgVFVV']

# DECRYPTED LIST OF MSGs
j = [base64.b64decode(item).decode("utf-8") for item in j]
k = [base64.b64decode(item).decode("utf-8") for item in k]
l = [base64.b64decode(item).decode("utf-8") for item in l]

def main():

    print('''                    DISCLAIMER!  READ THE FOLLOWING BEFORE RUNNING                         
    This Program helps you to abuse a guy for revenge so Do it on your own RISK! xD
    remember!!!!! this program uses pyautogui so your cursor should be ready after running it
    Meanwhile, your cursor should be in the text field where the program will start sending messages\n''')

    username = input("For whom you are going to abuse gimme username/name of that human: ")
    print("\n LONG PRESS 'Esc' or 'End' BUTTON TO STOP THE PROGRAM or MOVE YOUR MOUSE CURSOR TO ANY CORNER OF THE SCREEN      ")
    wait = input("Prompt how much seconds of delay per msg? Default=2 : ")
    if wait == "":
        wait = 2
    else:
        wait = int(wait)
    
    sleep(5)   # 5 seconds wait before spamming msgs

    try:
        for gali in j:
            if (keyboard.is_pressed("esc") or keyboard.is_pressed("end")):
                print("Program exited! Goodbye..")   # exit the loop if you long press Esc or End key
                break
            else:
                write(f"{username} {gali}")
                press("enter")
                sleep(wait) # wait after one msg

    except KeyboardInterrupt:
        print("ok goodbye...")    # if ctrl + c is pressed on terminal 
        
    except FailSafeException:
        print("ok goodbye...")    # if you move your mouse cursor to the corner of the screen
        

if __name__ == "__main__":
    main()
