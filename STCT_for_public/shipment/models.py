from django.db import models                                #揚げ地、客情報追加必要

                                                            #メーカーについてはカテゴリーを設定しようと思ったが止めた。
                                                            #毎年大なり小なり新規メーカーが出ては消えているので
                                                            #その都度追加するのは非現実的。
class InfoModel(models.Model):
    consignee = models.ForeignKey('auth.User',
        on_delete=models.CASCADE,null=True)                 #客
    shipper_name = models.CharField(max_length=25)          #シッパー名
    depdate_from_ru = models.DateField()                    #現地出荷日
    spec_no = models.CharField(max_length=12)               #スペックNo、代替No
    cntr_no = models.CharField(max_length=12)               #コンテナNo
    cube_m3 = models.FloatField()                           #材積数量
    cntr_eta = models.DateField(null=True)                  #コンテナETA  
    vessel_name = models.CharField(max_length=25)           #船名
    bool_eta = models.BooleanField(verbose_name = "到着済", 
        default=False)                                      #到着したか否か
    final_update = models.DateField(auto_now=True)          #最終更新日
    option = models.TextField(null=True)                    #備考欄
    item_property = models.CharField(max_length=25)         #アイテム明細

    def __str__(self):                                      #特殊メソッド
        return f"{self.consignee} {self. shipper_name} {self.spec_no} {self.cntr_no} {self.item_property}"