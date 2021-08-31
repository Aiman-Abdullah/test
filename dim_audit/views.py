from django.shortcuts import render
from django.shortcuts import render

from .models import stageProduct, tranProduct, dimProduct
from .resources import stageProductResource, tranProductResource, dimProductResource

from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime


from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/accounts/login/")
def simple_upload(request):
    if request.method == 'POST':

        # updating stage table
        stage_product_resource = stageProductResource()
        dataset = Dataset()
        new_stage_products = request.FILES['myfile']
        stageProductS = stageProduct.objects.all()
        stageProductS.delete()
        imported_data = dataset.load(new_stage_products.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
        	print(data[1])
        	value = stageProduct(
        		data[0],
        		data[1],
        		data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
        		data[8],
        		)
        	value.save()       

        #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now
        


        # updating transform tabel
        stageProducts = stageProduct.objects.all()
        length = stageProduct.objects.count()

        for i in range(0,len(stageProducts)):
            
            key = stageProducts[i].productid  
            if tranProduct.objects.filter(productid=key).exists(): 

                tranproduct = tranProduct.objects.filter(productid=key)

                description = stageProduct.objects.get(productid=key).description
                pdg = stageProduct.objects.get(productid=key).pdg
                producttype = stageProduct.objects.get(productid=key).producttype
                dtc = stageProduct.objects.get(productid=key).dtc
                mindeposit = stageProduct.objects.get(productid=key).mindeposit
                phaseoutdate = stageProduct.objects.get(productid=key).phaseoutdate
                discdate = stageProduct.objects.get(productid=key).discdate
                if discdate == None:
                    discontinued = "N"
                else:
                    discontinued = "Y"
                col = stageProduct.objects.get(productid=key).col
                rowiscurrent = "Y"
                rowenddate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                rowchangereason = "normal update"

                tranproduct.update(description=description, pdg=pdg, producttype= producttype
                                 , dtc =dtc , mindeposit = mindeposit
                                 , phaseoutdate = phaseoutdate, discdate = discdate, discontinued =discontinued, col = col
                                 , rowiscurrent = rowiscurrent, rowenddate = rowenddate, rowchangereason = rowchangereason)

            else:
                productid = stageProducts[i].productid
                description = stageProducts[i].description
                pdg = stageProducts[i].pdg
                producttype = stageProducts[i].producttype
                dtc = stageProducts[i].dtc
                mindeposit = stageProducts[i].mindeposit
                phaseoutdate = stageProducts[i].phaseoutdate
                discdate = stageProducts[i].discdate
                if discdate > '2000-01-01 00:00:00':
                    discontinued = "Y"
                else:
                    discontinued = "N"
                col = stageProducts[i].col
                rowiscurrent = "Y"
                rowstartdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                rowenddate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                rowchangereason = "original state"

                tranproduct = tranProduct(productid = productid, description = description, pdg = pdg
                                        , producttype = producttype, dtc = dtc, mindeposit = mindeposit
                                        , phaseoutdate = phaseoutdate, discdate = discdate, col = col
                                        , rowiscurrent = rowiscurrent, rowstartdate = rowstartdate, rowenddate = rowenddate
                                        , rowchangereason = rowchangereason
                                        )
                tranproduct.save()

        # loading to datawarehouse tabel
        tranProducts = tranProduct.objects.all()
        length = tranProduct.objects.count()

        for i in range(0,len(tranProducts)):
            
            key = tranProducts[i].productid  
            if dimProduct.objects.filter(productid=key).exists(): 

                dimproduct = dimProduct.objects.filter(productid=key)

                description = tranProduct.objects.get(productid=key).description
                pdg = tranProduct.objects.get(productid=key).pdg
                producttype = tranProduct.objects.get(productid=key).producttype
                dtc = tranProduct.objects.get(productid=key).dtc
                mindeposit = tranProduct.objects.get(productid=key).mindeposit
                phaseoutdate = tranProduct.objects.get(productid=key).phaseoutdate
                discdate = tranProduct.objects.get(productid=key).discdate
                discontinued = tranProduct.objects.get(productid=key).discontinued
                col = tranProduct.objects.get(productid=key).col
                rowiscurrent = tranProduct.objects.get(productid=key).rowiscurrent
                rowenddate = tranProduct.objects.get(productid=key).rowenddate
                rowchangereason = "normal update"

                dimproduct.update(description=description, pdg=pdg, producttype= producttype
                                 , dtc =dtc , mindeposit = mindeposit
                                 , phaseoutdate = phaseoutdate, discdate = discdate, discontinued =discontinued, col = col
                                 , rowiscurrent = rowiscurrent, rowenddate = rowenddate, rowchangereason = rowchangereason)

            else:
                productid = tranProducts[i].productid
                description = tranProducts[i].description
                pdg = tranProducts[i].pdg
                producttype = tranProducts[i].producttype
                dtc = tranProducts[i].dtc
                mindeposit = tranProducts[i].mindeposit
                phaseoutdate = tranProducts[i].phaseoutdate
                discdate = tranProducts[i].discdate
                discontinued = tranProducts[i].discontinued
                col = tranProducts[i].col
                rowiscurrent = tranProducts[i].discontinued
                rowstartdate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                rowenddate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                rowchangereason = "original state"

                dimproduct = dimProduct(productid = productid, description = description, pdg = pdg
                                        , producttype = producttype, dtc = dtc, mindeposit = mindeposit
                                        , phaseoutdate = phaseoutdate, discdate = discdate, discontinued =discontinued, col = col
                                        , rowiscurrent = rowiscurrent, rowstartdate = rowstartdate, rowenddate = rowenddate
                                        , rowchangereason = rowchangereason
                                        )
                dimproduct.save() 

    return render(request, 'dimProductInput.html')
