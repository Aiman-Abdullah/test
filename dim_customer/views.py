from django.shortcuts import render, redirect
from django.shortcuts import render

from .models import Stage_customer, Tran_customer, Dim_customer
from dim_table.models import Dim_table
from .resources import Stage_customer_resource, Tran_customer_resource, Dim_customer_resource

from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime

import pandas as pd
from django_pandas.io import read_frame

from django.contrib import messages
from datetime import datetime

from django.contrib.auth.decorators import login_required

# Create your views here.
app_start_time = datetime.now()
@login_required(login_url="/accounts/login/")
def simple_upload(request):

    if request.method == 'POST':

        app_start_time = datetime.now()

        # updating stage table
        stage_customer_resource = Stage_customer_resource()
        dataset = Dataset()
        new_stage_customers = request.FILES['myfile']
        stage_customers = Stage_customer.objects.all()
        stage_customers.delete()
        imported_data = dataset.load(new_stage_customers.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
        	print(data[1])
        	value = Stage_customer(
        		data[0]
        	,	data[1]
        	,	data[2]
            ,	data[3]
            ,	data[4]
            ,	data[5]
            # ,	data[6]
            # ,	data[7]
            # ,	data[8]
            ,	data[9]
            ,	data[10]
        	,	data[11]
        	,	data[12]
            ,	data[13]
            # ,	data[14]
            # ,	data[15]
            ,	data[16]
            ,	data[17]
            ,	data[18]
            ,	data[19]
            # ,	data[20]
        	# ,	data[21]
        	,	data[22]
            # ,	data[23]
            # ,	data[24]
            # ,	data[25]
            ,	data[26]
            ,	data[27]
            ,	data[28]
            ,	data[29]
            ,	data[30]
        	,	data[31]
        	,	data[32]
            ,	data[33]
            ,	data[34]
            ,	data[35]
            ,	data[36]
            ,	data[37]
            ,	data[38]
            ,	data[39]
            ,	data[40]
        	,	data[41]
        	,	data[42]
            ,	data[43]
            ,	data[44]
            ,	data[45]
            ,	data[46]
            ,	data[47]
            ,	data[48]
            ,	data[49]
            # ,	data[50]
        	,	data[51]
        	,	data[52]
            ,	data[53]
            # ,	data[54]
            ,	data[55]
            ,	data[56]
            ,	data[57]
            ,	data[58]
            ,	data[59]
            ,	data[60]
        	# ,	data[61]
        	,	data[62]
            ,	data[63]
            ,	data[64]
            ,	data[65]
            ,	data[66]
            ,	data[67]
            ,	data[68]
            ,	data[69]
            # ,	data[70]
        	# ,	data[71]
        	# ,	data[72]
            ,	data[73]
            ,	data[74]
            ,	data[75]
            ,	data[76]
            ,	data[77]
            ,	data[78]
            ,	data[79]
            # ,	data[80]
        	# ,	data[81]
        	,	data[82]
            ,	data[83]
            ,	data[84]
            ,	data[85]
            ,	data[86]
            ,	data[87]
            ,	data[88]
            ,	data[89]
            # ,	data[90]
        	,	data[91]
        	,	data[92]
            ,	data[93]
            ,	data[94]
            ,	data[95]
            ,	data[96]
            # ,	data[97]
            # ,	data[98]
            # ,	data[99]
            # ,	data[100]
        	# ,	data[101]
        	# ,	data[102]
            # ,	data[103]
            # ,	data[104]
            # ,	data[105]
            # ,	data[106]
            ,	data[107]
            ,	data[108]
            # ,	data[109]
            ,	data[110]
        	,	data[111]
        	# ,	data[112]
            # ,	data[113]
            # ,	data[114]
            # ,	data[115]
            # ,	data[116]
            # ,	data[117]
            # ,	data[118]
            # ,	data[119]
            # ,	data[120]
        	# ,	data[121]
        	# ,	data[122]
            # ,	data[123]
            # ,	data[124]
            # ,	data[125]
            # ,	data[126]
            # ,	data[127]
            # ,	data[128]
            # ,	data[129]
            # ,	data[130]
        	# ,	data[131]
        	# ,	data[132]
            # ,	data[133]
            # ,	data[134]
            # ,	data[135]
            # ,	data[136]
            # ,	data[137]
            # ,	data[138]
            # ,	data[139]
            # ,	data[140]
        	# ,	data[141]
        	# ,	data[142]
            # ,	data[143]
            # ,	data[144]
            # ,	data[145]
            # ,	data[146]
            # ,	data[147]
            # ,	data[148]
            # ,	data[149]
            # ,	data[150]
        	# ,	data[151]
        	# ,	data[152]
            # ,	data[153]
            # ,	data[154]
            # ,	data[155]
            ,	data[156]
            ,	data[157]
            ,	data[158]
            # ,	data[159]
            # ,	data[160]
        	# ,	data[161]
        	# ,	data[162]
            # ,	data[163]
            # ,	data[164]
            # ,	data[165]
            # ,	data[166]
            # ,	data[167]
            # ,	data[168]
            # ,	data[169]
            # ,	data[170]
        	# ,	data[171]
        	# ,	data[172]
            # ,	data[173]
            # ,	data[174]
            # ,	data[175]
            # ,	data[176]
            # ,	data[177]
            # ,	data[178]
            # ,	data[179]
            ,	data[180]
            ,	data[181]
            ,	data[182]
            ,	data[183]
            ,
        	)
        	value.save()       

        #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now
        
        # updating transform table

        # clearing transform table for new data
        tran_customers = Tran_customer.objects.all()
        tran_customers.delete()
        
        # if Stage_customer.objects.filter(customer_account=''): 

        #         stage_customer = Stage_customer.objects.filter(customer_account='')
        #         stage_customer.delete()


        stage_customers = Stage_customer.objects.all()
        length = Stage_customer.objects.count()
        print(str(len(stage_customers))+' length of stage customer')

        # for i in range(0,len(stage_customers)-1):
        #     day = stage_customers[i].customer_account  
        #     if day == "0000-00-00":
        #         day = "2000-01-01"

        for i in range(0,len(stage_customers)):
  
            key = stage_customers[i].customer_account  
            if Tran_customer.objects.filter(customer_account=key).exists(): 

                tran_customer = Tran_customer.objects.filter(customer_account=key)

                #customer_account = Stage_customer.objects.get(customer_account=key).customer_account
                customer_business_person = Stage_customer.objects.get(customer_account=key).customer_business_person
                customer_name = Stage_customer.objects.get(customer_account=key).customer_name
                customer_primary_phone = Stage_customer.objects.get(customer_account=key).customer_primary_phone
                customer_zip = Stage_customer.objects.get(customer_account=key).customer_zip
                customer_street_1 = Stage_customer.objects.get(customer_account=key).customer_street_1
                # customer_street_2 = Stage_customer.objects.get(customer_account=key).customer_street_2
                # customer_street_3 = Stage_customer.objects.get(customer_account=key).customer_street_3
                # customer_street_4 = Stage_customer.objects.get(customer_account=key).customer_street_4
                customer_city = Stage_customer.objects.get(customer_account=key).customer_city
                customer_state = Stage_customer.objects.get(customer_account=key).customer_state
                customer_country = Stage_customer.objects.get(customer_account=key).customer_country
                customer_address_type = Stage_customer.objects.get(customer_account=key).customer_address_type
                customer_address_fax = Stage_customer.objects.get(customer_account=key).customer_address_fax
                # customer_country_code = Stage_customer.objects.get(customer_account=key).customer_country_code
                # customer_idd_prefix = Stage_customer.objects.get(customer_account=key).customer_idd_prefix
                customer_account_activation_email = Stage_customer.objects.get(customer_account=key).customer_account_activation_email
                customer_advance_ship_notice = Stage_customer.objects.get(customer_account=key).customer_advance_ship_notice
                customer_order_submittal = Stage_customer.objects.get(customer_account=key).customer_order_submittal
                customer_email_subscription = Stage_customer.objects.get(customer_account=key).customer_email_subscription
                # customer_website = Stage_customer.objects.get(customer_account=key).customer_website
                # customer_customer_reference = Stage_customer.objects.get(customer_account=key).customer_customer_reference
                customer_default_order_comments = Stage_customer.objects.get(customer_account=key).customer_default_order_comments
                customer_default_invoice_comments = Stage_customer.objects.get(customer_account=key).customer_default_invoice_comments
                # customer_hide_cost_on_order_confirmation = Stage_customer.objects.get(customer_account=key).customer_hide_cost_on_order_confirmation
                # customer_allow_duplicate_po = Stage_customer.objects.get(customer_account=key).customer_allow_duplicate_po
                customer_first_name_last_name = Stage_customer.objects.get(customer_account=key).customer_first_name_last_name
                customer_work_phone = Stage_customer.objects.get(customer_account=key).customer_work_phone
                customer_ext = Stage_customer.objects.get(customer_account=key).customer_ext
                customer_cell_phone = Stage_customer.objects.get(customer_account=key).customer_cell_phone
                customer_home_phone = Stage_customer.objects.get(customer_account=key).customer_home_phone
                customer_fax = Stage_customer.objects.get(customer_account=key).customer_fax
                customer_corporate_account = Stage_customer.objects.get(customer_account=key).customer_corporate_account
                customer_email_credit_hold = Stage_customer.objects.get(customer_account=key).customer_email_credit_hold
                customer_credit_hold_email = Stage_customer.objects.get(customer_account=key).customer_credit_hold_email
                customer_art_hold_email = Stage_customer.objects.get(customer_account=key).customer_art_hold_email
                customer_email_invoice = Stage_customer.objects.get(customer_account=key).customer_email_invoice
                customer_invoice_notification = Stage_customer.objects.get(customer_account=key).customer_invoice_notification
                customer_email_invoice_past_due_alert = Stage_customer.objects.get(customer_account=key).customer_email_invoice_past_due_alert
                customer_invoice_past_due_alert = Stage_customer.objects.get(customer_account=key).customer_invoice_past_due_alert
                customer_email_statement = Stage_customer.objects.get(customer_account=key).customer_email_statement
                customer_statements = Stage_customer.objects.get(customer_account=key).customer_statements
                customer_email_credit_memo = Stage_customer.objects.get(customer_account=key).customer_email_credit_memo
                customer_credit_memo_email = Stage_customer.objects.get(customer_account=key).customer_credit_memo_email
                customer_email_return_reminder = Stage_customer.objects.get(customer_account=key).customer_email_return_reminder
                customer_return_reminder_email = Stage_customer.objects.get(customer_account=key).customer_return_reminder_email
                customer_reference_associate_email = Stage_customer.objects.get(customer_account=key).customer_reference_associate_email
                customer_fed_tax_code = Stage_customer.objects.get(customer_account=key).customer_fed_tax_code
                customer_fed_tax_freight = Stage_customer.objects.get(customer_account=key).customer_fed_tax_freight
                customer_fed_exempt_number = Stage_customer.objects.get(customer_account=key).customer_fed_exempt_number
                # customer_signed_fed_certificate = Stage_customer.objects.get(customer_account=key).customer_signed_fed_certificate
                customer_state_tax_code = Stage_customer.objects.get(customer_account=key).customer_state_tax_code
                customer_state_tax_freight = Stage_customer.objects.get(customer_account=key).customer_state_tax_freight
                customer_state_exempt_number = Stage_customer.objects.get(customer_account=key).customer_state_exempt_number
                # customer_signed_state_certificate = Stage_customer.objects.get(customer_account=key).customer_signed_state_certificate
                customer_warehouse = Stage_customer.objects.get(customer_account=key).customer_warehouse
                customer_site = Stage_customer.objects.get(customer_account=key).customer_site
                customer_type = Stage_customer.objects.get(customer_account=key).customer_type
                customer_territory = Stage_customer.objects.get(customer_account=key).customer_territory
                customer_site_number = Stage_customer.objects.get(customer_account=key).customer_site_number
                customer_source = Stage_customer.objects.get(customer_account=key).customer_source
                # customer_royalty_included = Stage_customer.objects.get(customer_account=key).customer_royalty_included
                customer_route_codes = Stage_customer.objects.get(customer_account=key).customer_route_codes
                customer_route_sequence = Stage_customer.objects.get(customer_account=key).customer_route_sequence
                customer_ship_via = Stage_customer.objects.get(customer_account=key).customer_ship_via
                customer_price_suffix = Stage_customer.objects.get(customer_account=key).customer_price_suffix
                customer_drop_ship = Stage_customer.objects.get(customer_account=key).customer_drop_ship
                customer_high_low_discount = Stage_customer.objects.get(customer_account=key).customer_high_low_discount
                customer_bill_to_name = Stage_customer.objects.get(customer_account=key).customer_bill_to_name
                customer_bill_to_street_1 = Stage_customer.objects.get(customer_account=key).customer_bill_to_street_1
                # customer_bill_to_street_2 = Stage_customer.objects.get(customer_account=key).customer_bill_to_street_2
                # customer_bill_to_street_3 = Stage_customer.objects.get(customer_account=key).customer_bill_to_street_3
                # customer_bill_to_street_4 = Stage_customer.objects.get(customer_account=key).customer_bill_to_street_4
                customer_bill_to_city = Stage_customer.objects.get(customer_account=key).customer_bill_to_city
                customer_bill_to_state = Stage_customer.objects.get(customer_account=key).customer_bill_to_state
                customer_bill_to_zipcode = Stage_customer.objects.get(customer_account=key).customer_bill_to_zipcode
                customer_bill_to_country = Stage_customer.objects.get(customer_account=key).customer_bill_to_country
                customer_bill_to_phone = Stage_customer.objects.get(customer_account=key).customer_bill_to_phone
                customer_bill_to_fax = Stage_customer.objects.get(customer_account=key).customer_bill_to_fax
                customer_opened = Stage_customer.objects.get(customer_account=key).customer_opened
                # customer_last_invoice = Stage_customer.objects.get(customer_account=key).customer_last_invoice
                # customer_last_payment = Stage_customer.objects.get(customer_account=key).customer_last_payment
                customer_terms = Stage_customer.objects.get(customer_account=key).customer_terms
                customer_days = Stage_customer.objects.get(customer_account=key).customer_days
                customer_other = Stage_customer.objects.get(customer_account=key).customer_other
                customer_past_due_max = Stage_customer.objects.get(customer_account=key).customer_past_due_max
                customer_invoice_due_days = Stage_customer.objects.get(customer_account=key).customer_invoice_due_days
                customer_cod = Stage_customer.objects.get(customer_account=key).customer_cod
                customer_prepay_cc = Stage_customer.objects.get(customer_account=key).customer_prepay_cc
                customer_charge_freight = Stage_customer.objects.get(customer_account=key).customer_charge_freight
                # customer_collector = Stage_customer.objects.get(customer_account=key).customer_collector
                customer_credit_hold_code = Stage_customer.objects.get(customer_account=key).customer_credit_hold_code
                customer_credit_limit = Stage_customer.objects.get(customer_account=key).customer_credit_limit
                customer_last_reviewed = Stage_customer.objects.get(customer_account=key).customer_last_reviewed
                customer_include_remakes = Stage_customer.objects.get(customer_account=key).customer_include_remakes
                customer_on_any_order_lower = Stage_customer.objects.get(customer_account=key).customer_on_any_order_lower
                customer_on_any_order_higher = Stage_customer.objects.get(customer_account=key).customer_on_any_order_higher
                # customer_current_lower = Stage_customer.objects.get(customer_account=key).customer_current_lower
                # customer_current_higher = Stage_customer.objects.get(customer_account=key).customer_current_higher
                # customer_30_days_ar_lower = Stage_customer.objects.get(customer_account=key).customer_30_days_ar_lower
                # customer_30_days_ar_higher = Stage_customer.objects.get(customer_account=key).customer_30_days_ar_higher
                # customer_60_days_ar_lower = Stage_customer.objects.get(customer_account=key).customer_60_days_ar_lower
                # customer_60_days_ar_higher = Stage_customer.objects.get(customer_account=key).customer_60_days_ar_higher
                # customer_90_days_ar_lower = Stage_customer.objects.get(customer_account=key).customer_90_days_ar_lower
                # customer_90_days_ar_higher = Stage_customer.objects.get(customer_account=key).customer_90_days_ar_higher
                # customer_120_days_ar_lower = Stage_customer.objects.get(customer_account=key).customer_120_days_ar_lower
                # customer_120_days_ar_higher = Stage_customer.objects.get(customer_account=key).customer_120_days_ar_higher
                customer_reference_1 = Stage_customer.objects.get(customer_account=key).customer_reference_1
                customer_waive_minimum_deposit = Stage_customer.objects.get(customer_account=key).customer_waive_minimum_deposit
                # customer_reference_2 = Stage_customer.objects.get(customer_account=key).customer_reference_2
                customer_account_suspended = Stage_customer.objects.get(customer_account=key).customer_account_suspended
                customer_saleperson_1 = Stage_customer.objects.get(customer_account=key).customer_saleperson_1
                # customer_saleperson_2 = Stage_customer.objects.get(customer_account=key).customer_saleperson_2
                # customer_saleperson_3 = Stage_customer.objects.get(customer_account=key).customer_saleperson_3
                # customer_saleperson_4 = Stage_customer.objects.get(customer_account=key).customer_saleperson_4
                # customer_saleperson_5 = Stage_customer.objects.get(customer_account=key).customer_saleperson_5
                # customer_constant_1 = Stage_customer.objects.get(customer_account=key).customer_constant_1
                # customer_constant_2 = Stage_customer.objects.get(customer_account=key).customer_constant_2
                # customer_constant_3 = Stage_customer.objects.get(customer_account=key).customer_constant_3
                # customer_constant_4 = Stage_customer.objects.get(customer_account=key).customer_constant_4
                # customer_constant_5 = Stage_customer.objects.get(customer_account=key).customer_constant_5
                # customer_constant_6 = Stage_customer.objects.get(customer_account=key).customer_constant_6
                # customer_constant_7 = Stage_customer.objects.get(customer_account=key).customer_constant_7
                # customer_constant_8 = Stage_customer.objects.get(customer_account=key).customer_constant_8
                # customer_constant_9 = Stage_customer.objects.get(customer_account=key).customer_constant_9
                # customer_constant_10 = Stage_customer.objects.get(customer_account=key).customer_constant_10
                # customer_constant_11 = Stage_customer.objects.get(customer_account=key).customer_constant_11
                # customer_constant_12 = Stage_customer.objects.get(customer_account=key).customer_constant_12
                # customer_constant_13 = Stage_customer.objects.get(customer_account=key).customer_constant_13
                # customer_constant_14 = Stage_customer.objects.get(customer_account=key).customer_constant_14
                # customer_constant_15 = Stage_customer.objects.get(customer_account=key).customer_constant_15
                # customer_constant_16 = Stage_customer.objects.get(customer_account=key).customer_constant_16
                # customer_constant_17 = Stage_customer.objects.get(customer_account=key).customer_constant_17
                # customer_constant_18 = Stage_customer.objects.get(customer_account=key).customer_constant_18
                # customer_constant_19 = Stage_customer.objects.get(customer_account=key).customer_constant_19
                # customer_constant_20 = Stage_customer.objects.get(customer_account=key).customer_constant_20
                # user_defined_1 = Stage_customer.objects.get(customer_account=key).user_defined_1
                # user_defined_2 = Stage_customer.objects.get(customer_account=key).user_defined_2
                # user_defined_3 = Stage_customer.objects.get(customer_account=key).user_defined_3
                # user_defined_4 = Stage_customer.objects.get(customer_account=key).user_defined_4
                # user_defined_5 = Stage_customer.objects.get(customer_account=key).user_defined_5
                # user_defined_6 = Stage_customer.objects.get(customer_account=key).user_defined_6
                # user_defined_7 = Stage_customer.objects.get(customer_account=key).user_defined_7
                # user_defined_8 = Stage_customer.objects.get(customer_account=key).user_defined_8
                # user_defined_9 = Stage_customer.objects.get(customer_account=key).user_defined_9
                # user_defined_10 = Stage_customer.objects.get(customer_account=key).user_defined_10
                # user_defined_11 = Stage_customer.objects.get(customer_account=key).user_defined_11
                # user_defined_12 = Stage_customer.objects.get(customer_account=key).user_defined_12
                # user_defined_13 = Stage_customer.objects.get(customer_account=key).user_defined_13
                # user_defined_14 = Stage_customer.objects.get(customer_account=key).user_defined_14
                # user_defined_15 = Stage_customer.objects.get(customer_account=key).user_defined_15
                # user_defined_16 = Stage_customer.objects.get(customer_account=key).user_defined_16
                # user_defined_17 = Stage_customer.objects.get(customer_account=key).user_defined_17
                # user_defined_18 = Stage_customer.objects.get(customer_account=key).user_defined_18
                # user_defined_19 = Stage_customer.objects.get(customer_account=key).user_defined_19
                # user_defined_20 = Stage_customer.objects.get(customer_account=key).user_defined_20
                customer_customer_w_tax = Stage_customer.objects.get(customer_account=key).customer_customer_w_tax
                customer_limit_number_of_dealer_logins_to = Stage_customer.objects.get(customer_account=key).customer_limit_number_of_dealer_logins_to
                customer_days_to_hold_quotes = Stage_customer.objects.get(customer_account=key).customer_days_to_hold_quotes
                # customer_enable_price_calculation = Stage_customer.objects.get(customer_account=key).customer_enable_price_calculation
                # customer_enable_freight_calculation = Stage_customer.objects.get(customer_account=key).customer_enable_freight_calculation
                # customer_collection_display = Stage_customer.objects.get(customer_account=key).customer_collection_display
                # customer_internal_xml_id = Stage_customer.objects.get(customer_account=key).customer_internal_xml_id
                # customer_client_quote_letter_verbiage = Stage_customer.objects.get(customer_account=key).customer_client_quote_letter_verbiage
                # customer_booked_orders = Stage_customer.objects.get(customer_account=key).customer_booked_orders
                # customer_deposits = Stage_customer.objects.get(customer_account=key).customer_deposits
                # customer_balance_due = Stage_customer.objects.get(customer_account=key).customer_balance_due
                # customer_open_ar = Stage_customer.objects.get(customer_account=key).customer_open_ar
                # customer_30_day_ar = Stage_customer.objects.get(customer_account=key).customer_30_day_ar
                # customer_60_day_ar = Stage_customer.objects.get(customer_account=key).customer_60_day_ar
                # customer_90_day_ar = Stage_customer.objects.get(customer_account=key).customer_90_day_ar
                # customer_120_day_ar = Stage_customer.objects.get(customer_account=key).customer_120_day_ar
                # customer_unapplied = Stage_customer.objects.get(customer_account=key).customer_unapplied
                # customer_total_open_ar = Stage_customer.objects.get(customer_account=key).customer_total_open_ar
                # customer_ytd = Stage_customer.objects.get(customer_account=key).customer_ytd
                # customer_previous_year = Stage_customer.objects.get(customer_account=key).customer_previous_year
                # customer_high_sale = Stage_customer.objects.get(customer_account=key).customer_high_sale
                # customer_py_high_sale = Stage_customer.objects.get(customer_account=key).customer_py_high_sale
                # customer_cogs = Stage_customer.objects.get(customer_account=key).customer_cogs
                # customer_py_cogs = Stage_customer.objects.get(customer_account=key).customer_py_cogs
                customer_avg_days_to_pay = Stage_customer.objects.get(customer_account=key).customer_avg_days_to_pay
                customer_pv_avg_days_to_pay = Stage_customer.objects.get(customer_account=key).customer_pv_avg_days_to_pay
                customer_times_past_due = Stage_customer.objects.get(customer_account=key).customer_times_past_due
                customer_py_times_past_due = Stage_customer.objects.get(customer_account=key).customer_py_times_past_due


                row_is_current = "Y"
                row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_change_reason = "normal update"

                tran_customer.update(#customer_account=customer_account,
                                   customer_business_person=customer_business_person
                                 , customer_name= customer_name
                                 , customer_primary_phone = customer_primary_phone
                                 , customer_zip = customer_zip
                                 , customer_street_1 = customer_street_1
                                #  , customer_street_2 = customer_street_2
                                #  , customer_street_3 = customer_street_3
                                #  , customer_street_4 = customer_street_4
                                 , customer_city = customer_city
                                 , customer_state = customer_state
                                 , customer_country = customer_country
                                 , customer_address_type = customer_address_type
                                 , customer_address_fax = customer_address_fax
                                #  , customer_country_code = customer_country_code
                                #  , customer_idd_prefix = customer_idd_prefix
                                 , customer_account_activation_email = customer_account_activation_email
                                 , customer_advance_ship_notice = customer_advance_ship_notice
                                 , customer_order_submittal = customer_order_submittal
                                 , customer_email_subscription = customer_email_subscription
                                #  , customer_website = customer_website
                                #  , customer_customer_reference = customer_customer_reference
                                 , customer_default_order_comments = customer_default_order_comments
                                 , customer_default_invoice_comments = customer_default_invoice_comments
                                #  , customer_hide_cost_on_order_confirmation = customer_hide_cost_on_order_confirmation
                                #  , customer_allow_duplicate_po = customer_allow_duplicate_po
                                 , customer_first_name_last_name = customer_first_name_last_name
                                 , customer_work_phone = customer_work_phone
                                 , customer_ext = customer_ext
                                 , customer_cell_phone = customer_cell_phone
                                 , customer_home_phone = customer_home_phone
                                 , customer_fax = customer_fax
                                 , customer_corporate_account = customer_corporate_account
                                 , customer_email_credit_hold = customer_email_credit_hold
                                 , customer_credit_hold_email = customer_credit_hold_email
                                 , customer_art_hold_email = customer_art_hold_email
                                 , customer_email_invoice = customer_email_invoice
                                 , customer_invoice_notification = customer_invoice_notification
                                 , customer_email_invoice_past_due_alert = customer_email_invoice_past_due_alert
                                 , customer_invoice_past_due_alert = customer_invoice_past_due_alert
                                 , customer_email_statement = customer_email_statement
                                 , customer_statements = customer_statements
                                 , customer_email_credit_memo = customer_email_credit_memo
                                 , customer_credit_memo_email = customer_credit_memo_email
                                 , customer_email_return_reminder = customer_email_return_reminder
                                 , customer_return_reminder_email = customer_return_reminder_email
                                 , customer_reference_associate_email = customer_reference_associate_email
                                 , customer_fed_tax_code = customer_fed_tax_code
                                 , customer_fed_tax_freight = customer_fed_tax_freight
                                 , customer_fed_exempt_number = customer_fed_exempt_number
                                #  , customer_signed_fed_certificate = customer_signed_fed_certificate
                                 , customer_state_tax_code = customer_state_tax_code
                                 , customer_state_tax_freight = customer_state_tax_freight
                                 , customer_state_exempt_number = customer_state_exempt_number
                                #  , customer_signed_state_certificate = customer_signed_state_certificate
                                 , customer_warehouse = customer_warehouse
                                 , customer_site = customer_site
                                 , customer_type = customer_type
                                 , customer_territory = customer_territory
                                 , customer_site_number = customer_site_number
                                 , customer_source = customer_source
                                #  , customer_royalty_included = customer_royalty_included
                                 , customer_route_codes = customer_route_codes
                                 , customer_route_sequence = customer_route_sequence
                                 , customer_ship_via = customer_ship_via
                                 , customer_price_suffix = customer_price_suffix
                                 , customer_drop_ship = customer_drop_ship
                                 , customer_high_low_discount = customer_high_low_discount
                                 , customer_bill_to_name = customer_bill_to_name
                                 , customer_bill_to_street_1 = customer_bill_to_street_1
                                #  , customer_bill_to_street_2 = customer_bill_to_street_2
                                #  , customer_bill_to_street_3 = customer_bill_to_street_3
                                #  , customer_bill_to_street_4 = customer_bill_to_street_4
                                 , customer_bill_to_city = customer_bill_to_city
                                 , customer_bill_to_state = customer_bill_to_state
                                 , customer_bill_to_zipcode = customer_bill_to_zipcode
                                 , customer_bill_to_country = customer_bill_to_country
                                 , customer_bill_to_phone = customer_bill_to_phone
                                 , customer_bill_to_fax = customer_bill_to_fax
                                 , customer_opened = customer_opened
                                #  , customer_last_invoice = customer_last_invoice
                                #  , customer_last_payment = customer_last_payment
                                 , customer_terms = customer_terms
                                 , customer_days = customer_days
                                 , customer_other = customer_other
                                 , customer_past_due_max = customer_past_due_max
                                 , customer_invoice_due_days = customer_invoice_due_days
                                 , customer_cod = customer_cod
                                 , customer_prepay_cc = customer_prepay_cc
                                 , customer_charge_freight = customer_charge_freight
                                #  , customer_collector = customer_collector
                                 , customer_credit_hold_code = customer_credit_hold_code
                                 , customer_credit_limit = customer_credit_limit
                                 , customer_last_reviewed = customer_last_reviewed
                                 , customer_include_remakes = customer_include_remakes
                                 , customer_on_any_order_lower = customer_on_any_order_lower
                                 , customer_on_any_order_higher = customer_on_any_order_higher
                                #  , customer_current_lower = customer_current_lower
                                #  , customer_current_higher = customer_current_higher
                                #  , customer_30_days_ar_lower = customer_30_days_ar_lower
                                #  , customer_30_days_ar_higher = customer_30_days_ar_higher
                                #  , customer_60_days_ar_lower = customer_60_days_ar_lower
                                #  , customer_60_days_ar_higher = customer_60_days_ar_higher
                                #  , customer_90_days_ar_lower = customer_90_days_ar_lower
                                #  , customer_90_days_ar_higher = customer_90_days_ar_higher
                                #  , customer_120_days_ar_lower = customer_120_days_ar_lower
                                #  , customer_120_days_ar_higher = customer_120_days_ar_higher
                                 , customer_reference_1 = customer_reference_1
                                 , customer_waive_minimum_deposit = customer_waive_minimum_deposit
                                #  , customer_reference_2 = customer_reference_2
                                 , customer_account_suspended = customer_account_suspended
                                 , customer_saleperson_1 = customer_saleperson_1
                                #  , customer_saleperson_2 = customer_saleperson_2
                                #  , customer_saleperson_3 = customer_saleperson_3
                                #  , customer_saleperson_4 = customer_saleperson_4
                                #  , customer_saleperson_5 = customer_saleperson_5
                                #  , customer_constant_1 = customer_constant_1
                                #  , customer_constant_2 = customer_constant_2
                                #  , customer_constant_3 = customer_constant_3
                                #  , customer_constant_4 = customer_constant_4
                                #  , customer_constant_5 = customer_constant_5
                                #  , customer_constant_6 = customer_constant_6
                                #  , customer_constant_7 = customer_constant_7
                                #  , customer_constant_8 = customer_constant_8
                                #  , customer_constant_9 = customer_constant_9
                                #  , customer_constant_10 = customer_constant_10
                                #  , customer_constant_11 = customer_constant_11
                                #  , customer_constant_12 = customer_constant_12
                                #  , customer_constant_13 = customer_constant_13
                                #  , customer_constant_14 = customer_constant_14
                                #  , customer_constant_15 = customer_constant_15
                                #  , customer_constant_16 = customer_constant_16
                                #  , customer_constant_17 = customer_constant_17
                                #  , customer_constant_18 = customer_constant_18
                                #  , customer_constant_19 = customer_constant_19
                                #  , customer_constant_20 = customer_constant_20
                                #  , user_defined_1 = user_defined_1
                                #  , user_defined_2 = user_defined_2
                                #  , user_defined_3 = user_defined_3
                                #  , user_defined_4 = user_defined_4
                                #  , user_defined_5 = user_defined_5
                                #  , user_defined_6 = user_defined_6
                                #  , user_defined_7 = user_defined_7
                                #  , user_defined_8 = user_defined_8
                                #  , user_defined_9 = user_defined_9
                                #  , user_defined_10 = user_defined_10
                                #  , user_defined_11 = user_defined_11
                                #  , user_defined_12 = user_defined_12
                                #  , user_defined_13 = user_defined_13
                                #  , user_defined_14 = user_defined_14
                                #  , user_defined_15 = user_defined_15
                                #  , user_defined_16 = user_defined_16
                                #  , user_defined_17 = user_defined_17
                                #  , user_defined_18 = user_defined_18
                                #  , user_defined_19 = user_defined_19
                                #  , user_defined_20 = user_defined_20
                                 , customer_customer_w_tax = customer_customer_w_tax
                                 , customer_limit_number_of_dealer_logins_to = customer_limit_number_of_dealer_logins_to
                                 , customer_days_to_hold_quotes = customer_days_to_hold_quotes
                                #  , customer_enable_price_calculation = customer_enable_price_calculation
                                #  , customer_enable_freight_calculation = customer_enable_freight_calculation
                                #  , customer_collection_display = customer_collection_display
                                #  , customer_internal_xml_id = customer_internal_xml_id
                                #  , customer_client_quote_letter_verbiage = customer_client_quote_letter_verbiage
                                #  , customer_booked_orders = customer_booked_orders
                                #  , customer_deposits = customer_deposits
                                #  , customer_balance_due = customer_balance_due
                                #  , customer_open_ar = customer_open_ar
                                #  , customer_30_day_ar = customer_30_day_ar
                                #  , customer_60_day_ar = customer_60_day_ar
                                #  , customer_90_day_ar = customer_90_day_ar
                                #  , customer_120_day_ar = customer_120_day_ar
                                #  , customer_unapplied = customer_unapplied
                                #  , customer_total_open_ar = customer_total_open_ar
                                #  , customer_ytd = customer_ytd
                                #  , customer_previous_year = customer_previous_year
                                #  , customer_high_sale = customer_high_sale
                                #  , customer_py_high_sale = customer_py_high_sale
                                #  , customer_cogs = customer_cogs
                                #  , customer_py_cogs = customer_py_cogs
                                 , customer_avg_days_to_pay = customer_avg_days_to_pay
                                 , customer_pv_avg_days_to_pay = customer_pv_avg_days_to_pay
                                 , customer_times_past_due = customer_times_past_due
                                 , customer_py_times_past_due = customer_py_times_past_due


                                 , row_is_current = row_is_current, row_end_date = row_end_date, row_change_reason = row_change_reason)

            else:
                customer_account = stage_customers[i].customer_account
                customer_business_person = stage_customers[i].customer_business_person
                customer_name = stage_customers[i].customer_name
                customer_primary_phone = stage_customers[i].customer_primary_phone
                customer_zip = stage_customers[i].customer_zip
                customer_street_1 = stage_customers[i].customer_street_1
                # customer_street_2 = stage_customers[i].customer_street_2
                # customer_street_3 = stage_customers[i].customer_street_3
                # customer_street_4 = stage_customers[i].customer_street_4
                customer_city = stage_customers[i].customer_city
                customer_state = stage_customers[i].customer_state
                customer_country = stage_customers[i].customer_country
                customer_address_type = stage_customers[i].customer_address_type
                customer_address_fax = stage_customers[i].customer_address_fax
                # customer_country_code = stage_customers[i].customer_country_code
                # customer_idd_prefix = stage_customers[i].customer_idd_prefix
                customer_account_activation_email = stage_customers[i].customer_account_activation_email
                customer_advance_ship_notice = stage_customers[i].customer_advance_ship_notice
                customer_order_submittal = stage_customers[i].customer_order_submittal
                customer_email_subscription = stage_customers[i].customer_email_subscription
                # customer_website = stage_customers[i].customer_website
                # customer_customer_reference = stage_customers[i].customer_customer_reference
                customer_default_order_comments = stage_customers[i].customer_default_order_comments
                customer_default_invoice_comments = stage_customers[i].customer_default_invoice_comments
                # customer_hide_cost_on_order_confirmation = stage_customers[i].customer_hide_cost_on_order_confirmation
                # customer_allow_duplicate_po = stage_customers[i].customer_allow_duplicate_po
                customer_first_name_last_name = stage_customers[i].customer_first_name_last_name
                customer_work_phone = stage_customers[i].customer_work_phone
                customer_ext = stage_customers[i].customer_ext
                customer_cell_phone = stage_customers[i].customer_cell_phone
                customer_home_phone = stage_customers[i].customer_home_phone
                customer_fax = stage_customers[i].customer_fax
                customer_corporate_account = stage_customers[i].customer_corporate_account
                customer_email_credit_hold = stage_customers[i].customer_email_credit_hold
                customer_credit_hold_email = stage_customers[i].customer_credit_hold_email
                customer_art_hold_email = stage_customers[i].customer_art_hold_email
                customer_email_invoice = stage_customers[i].customer_email_invoice
                customer_invoice_notification = stage_customers[i].customer_invoice_notification
                customer_email_invoice_past_due_alert = stage_customers[i].customer_email_invoice_past_due_alert
                customer_invoice_past_due_alert = stage_customers[i].customer_invoice_past_due_alert
                customer_email_statement = stage_customers[i].customer_email_statement
                customer_statements = stage_customers[i].customer_statements
                customer_email_credit_memo = stage_customers[i].customer_email_credit_memo
                customer_credit_memo_email = stage_customers[i].customer_credit_memo_email
                customer_email_return_reminder = stage_customers[i].customer_email_return_reminder
                customer_return_reminder_email = stage_customers[i].customer_return_reminder_email
                customer_reference_associate_email = stage_customers[i].customer_reference_associate_email
                customer_fed_tax_code = stage_customers[i].customer_fed_tax_code
                customer_fed_tax_freight = stage_customers[i].customer_fed_tax_freight
                customer_fed_exempt_number = stage_customers[i].customer_fed_exempt_number
                # customer_signed_fed_certificate = stage_customers[i].customer_signed_fed_certificate
                customer_state_tax_code = stage_customers[i].customer_state_tax_code
                customer_state_tax_freight = stage_customers[i].customer_state_tax_freight
                customer_state_exempt_number = stage_customers[i].customer_state_exempt_number
                # customer_signed_state_certificate = stage_customers[i].customer_signed_state_certificate
                customer_warehouse = stage_customers[i].customer_warehouse
                customer_site = stage_customers[i].customer_site
                customer_type = stage_customers[i].customer_type
                customer_territory = stage_customers[i].customer_territory
                customer_site_number = stage_customers[i].customer_site_number
                customer_source = stage_customers[i].customer_source
                # customer_royalty_included = stage_customers[i].customer_royalty_included
                customer_route_codes = stage_customers[i].customer_route_codes
                customer_route_sequence = stage_customers[i].customer_route_sequence
                customer_ship_via = stage_customers[i].customer_ship_via
                customer_price_suffix = stage_customers[i].customer_price_suffix
                customer_drop_ship = stage_customers[i].customer_drop_ship
                customer_high_low_discount = stage_customers[i].customer_high_low_discount
                customer_bill_to_name = stage_customers[i].customer_bill_to_name
                customer_bill_to_street_1 = stage_customers[i].customer_bill_to_street_1
                # customer_bill_to_street_2 = stage_customers[i].customer_bill_to_street_2
                # customer_bill_to_street_3 = stage_customers[i].customer_bill_to_street_3
                # customer_bill_to_street_4 = stage_customers[i].customer_bill_to_street_4
                customer_bill_to_city = stage_customers[i].customer_bill_to_city
                customer_bill_to_state = stage_customers[i].customer_bill_to_state
                customer_bill_to_zipcode = stage_customers[i].customer_bill_to_zipcode
                customer_bill_to_country = stage_customers[i].customer_bill_to_country
                customer_bill_to_phone = stage_customers[i].customer_bill_to_phone
                customer_bill_to_fax = stage_customers[i].customer_bill_to_fax
                customer_opened = stage_customers[i].customer_opened
                if customer_opened == "0000-00-00":
                    customer_opened = "2000-01-01"
                # customer_last_invoice = stage_customers[i].customer_last_invoice
                # customer_last_payment = stage_customers[i].customer_last_payment
                customer_terms = stage_customers[i].customer_terms
                customer_days = stage_customers[i].customer_days
                customer_other = stage_customers[i].customer_other
                customer_past_due_max = stage_customers[i].customer_past_due_max
                customer_invoice_due_days = stage_customers[i].customer_invoice_due_days
                customer_cod = stage_customers[i].customer_cod
                customer_prepay_cc = stage_customers[i].customer_prepay_cc
                customer_charge_freight = stage_customers[i].customer_charge_freight
                # customer_collector = stage_customers[i].customer_collector
                customer_credit_hold_code = stage_customers[i].customer_credit_hold_code
                customer_credit_limit = stage_customers[i].customer_credit_limit
                customer_last_reviewed = stage_customers[i].customer_last_reviewed
                customer_include_remakes = stage_customers[i].customer_include_remakes
                customer_on_any_order_lower = stage_customers[i].customer_on_any_order_lower
                customer_on_any_order_higher = stage_customers[i].customer_on_any_order_higher
                # customer_current_lower = stage_customers[i].customer_current_lower
                # customer_current_higher = stage_customers[i].customer_current_higher
                # customer_30_days_ar_lower = stage_customers[i].customer_30_days_ar_lower
                # customer_30_days_ar_higher = stage_customers[i].customer_30_days_ar_higher
                # customer_60_days_ar_lower = stage_customers[i].customer_60_days_ar_lower
                # customer_60_days_ar_higher = stage_customers[i].customer_60_days_ar_higher
                # customer_90_days_ar_lower = stage_customers[i].customer_90_days_ar_lower
                # customer_90_days_ar_higher = stage_customers[i].customer_90_days_ar_higher
                # customer_120_days_ar_lower = stage_customers[i].customer_120_days_ar_lower
                # customer_120_days_ar_higher = stage_customers[i].customer_120_days_ar_higher
                customer_reference_1 = stage_customers[i].customer_reference_1
                customer_waive_minimum_deposit = stage_customers[i].customer_waive_minimum_deposit
                # customer_reference_2 = stage_customers[i].customer_reference_2
                customer_account_suspended = stage_customers[i].customer_account_suspended
                customer_saleperson_1 = stage_customers[i].customer_saleperson_1
                # customer_saleperson_2 = stage_customers[i].customer_saleperson_2
                # customer_saleperson_3 = stage_customers[i].customer_saleperson_3
                # customer_saleperson_4 = stage_customers[i].customer_saleperson_4
                # customer_saleperson_5 = stage_customers[i].customer_saleperson_5
                # customer_constant_1 = stage_customers[i].customer_constant_1
                # customer_constant_2 = stage_customers[i].customer_constant_2
                # customer_constant_3 = stage_customers[i].customer_constant_3
                # customer_constant_4 = stage_customers[i].customer_constant_4
                # customer_constant_5 = stage_customers[i].customer_constant_5
                # customer_constant_6 = stage_customers[i].customer_constant_6
                # customer_constant_7 = stage_customers[i].customer_constant_7
                # customer_constant_8 = stage_customers[i].customer_constant_8
                # customer_constant_9 = stage_customers[i].customer_constant_9
                # customer_constant_10 = stage_customers[i].customer_constant_10
                # customer_constant_11 = stage_customers[i].customer_constant_11
                # customer_constant_12 = stage_customers[i].customer_constant_12
                # customer_constant_13 = stage_customers[i].customer_constant_13
                # customer_constant_14 = stage_customers[i].customer_constant_14
                # customer_constant_15 = stage_customers[i].customer_constant_15
                # customer_constant_16 = stage_customers[i].customer_constant_16
                # customer_constant_17 = stage_customers[i].customer_constant_17
                # customer_constant_18 = stage_customers[i].customer_constant_18
                # customer_constant_19 = stage_customers[i].customer_constant_19
                # customer_constant_20 = stage_customers[i].customer_constant_20
                # user_defined_1 = stage_customers[i].user_defined_1
                # user_defined_2 = stage_customers[i].user_defined_2
                # user_defined_3 = stage_customers[i].user_defined_3
                # user_defined_4 = stage_customers[i].user_defined_4
                # user_defined_5 = stage_customers[i].user_defined_5
                # user_defined_6 = stage_customers[i].user_defined_6
                # user_defined_7 = stage_customers[i].user_defined_7
                # user_defined_8 = stage_customers[i].user_defined_8
                # user_defined_9 = stage_customers[i].user_defined_9
                # user_defined_10 = stage_customers[i].user_defined_10
                # user_defined_11 = stage_customers[i].user_defined_11
                # user_defined_12 = stage_customers[i].user_defined_12
                # user_defined_13 = stage_customers[i].user_defined_13
                # user_defined_14 = stage_customers[i].user_defined_14
                # user_defined_15 = stage_customers[i].user_defined_15
                # user_defined_16 = stage_customers[i].user_defined_16
                # user_defined_17 = stage_customers[i].user_defined_17
                # user_defined_18 = stage_customers[i].user_defined_18
                # user_defined_19 = stage_customers[i].user_defined_19
                # user_defined_20 = stage_customers[i].user_defined_20
                customer_customer_w_tax = stage_customers[i].customer_customer_w_tax
                customer_limit_number_of_dealer_logins_to = stage_customers[i].customer_limit_number_of_dealer_logins_to
                customer_days_to_hold_quotes = stage_customers[i].customer_days_to_hold_quotes
                # customer_enable_price_calculation = stage_customers[i].customer_enable_price_calculation
                # customer_enable_freight_calculation = stage_customers[i].customer_enable_freight_calculation
                # customer_collection_display = stage_customers[i].customer_collection_display
                # customer_internal_xml_id = stage_customers[i].customer_internal_xml_id
                # customer_client_quote_letter_verbiage = stage_customers[i].customer_client_quote_letter_verbiage
                # customer_booked_orders = stage_customers[i].customer_booked_orders
                # customer_deposits = stage_customers[i].customer_deposits
                # customer_balance_due = stage_customers[i].customer_balance_due
                # customer_open_ar = stage_customers[i].customer_open_ar
                # customer_30_day_ar = stage_customers[i].customer_30_day_ar
                # customer_60_day_ar = stage_customers[i].customer_60_day_ar
                # customer_90_day_ar = stage_customers[i].customer_90_day_ar
                # customer_120_day_ar = stage_customers[i].customer_120_day_ar
                # customer_unapplied = stage_customers[i].customer_unapplied
                # customer_total_open_ar = stage_customers[i].customer_total_open_ar
                # customer_ytd = stage_customers[i].customer_ytd
                # customer_previous_year = stage_customers[i].customer_previous_year
                # customer_high_sale = stage_customers[i].customer_high_sale
                # customer_py_high_sale = stage_customers[i].customer_py_high_sale
                # customer_cogs = stage_customers[i].customer_cogs
                # customer_py_cogs = stage_customers[i].customer_py_cogs
                customer_avg_days_to_pay = stage_customers[i].customer_avg_days_to_pay
                customer_pv_avg_days_to_pay = stage_customers[i].customer_pv_avg_days_to_pay
                customer_times_past_due = stage_customers[i].customer_times_past_due
                customer_py_times_past_due = stage_customers[i].customer_py_times_past_due




                row_is_current = "Y"
                row_start_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_change_reason = "original state"

                tran_customer = Tran_customer(
                                              customer_account=customer_account
                                            , customer_business_person=customer_business_person
                                            , customer_name= customer_name
                                            , customer_primary_phone = customer_primary_phone
                                            , customer_zip = customer_zip
                                            , customer_street_1 = customer_street_1
                                            #  , customer_street_2 = customer_street_2
                                            #  , customer_street_3 = customer_street_3
                                            #  , customer_street_4 = customer_street_4
                                            , customer_city = customer_city
                                            , customer_state = customer_state
                                            , customer_country = customer_country
                                            , customer_address_type = customer_address_type
                                            , customer_address_fax = customer_address_fax
                                            #  , customer_country_code = customer_country_code
                                            #  , customer_idd_prefix = customer_idd_prefix
                                            , customer_account_activation_email = customer_account_activation_email
                                            , customer_advance_ship_notice = customer_advance_ship_notice
                                            , customer_order_submittal = customer_order_submittal
                                            , customer_email_subscription = customer_email_subscription
                                            #  , customer_website = customer_website
                                            #  , customer_customer_reference = customer_customer_reference
                                            , customer_default_order_comments = customer_default_order_comments
                                            , customer_default_invoice_comments = customer_default_invoice_comments
                                            #  , customer_hide_cost_on_order_confirmation = customer_hide_cost_on_order_confirmation
                                            #  , customer_allow_duplicate_po = customer_allow_duplicate_po
                                            , customer_first_name_last_name = customer_first_name_last_name
                                            , customer_work_phone = customer_work_phone
                                            , customer_ext = customer_ext
                                            , customer_cell_phone = customer_cell_phone
                                            , customer_home_phone = customer_home_phone
                                            , customer_fax = customer_fax
                                            , customer_corporate_account = customer_corporate_account
                                            , customer_email_credit_hold = customer_email_credit_hold
                                            , customer_credit_hold_email = customer_credit_hold_email
                                            , customer_art_hold_email = customer_art_hold_email
                                            , customer_email_invoice = customer_email_invoice
                                            , customer_invoice_notification = customer_invoice_notification
                                            , customer_email_invoice_past_due_alert = customer_email_invoice_past_due_alert
                                            , customer_invoice_past_due_alert = customer_invoice_past_due_alert
                                            , customer_email_statement = customer_email_statement
                                            , customer_statements = customer_statements
                                            , customer_email_credit_memo = customer_email_credit_memo
                                            , customer_credit_memo_email = customer_credit_memo_email
                                            , customer_email_return_reminder = customer_email_return_reminder
                                            , customer_return_reminder_email = customer_return_reminder_email
                                            , customer_reference_associate_email = customer_reference_associate_email
                                            , customer_fed_tax_code = customer_fed_tax_code
                                            , customer_fed_tax_freight = customer_fed_tax_freight
                                            , customer_fed_exempt_number = customer_fed_exempt_number
                                            #  , customer_signed_fed_certificate = customer_signed_fed_certificate
                                            , customer_state_tax_code = customer_state_tax_code
                                            , customer_state_tax_freight = customer_state_tax_freight
                                            , customer_state_exempt_number = customer_state_exempt_number
                                            #  , customer_signed_state_certificate = customer_signed_state_certificate
                                            , customer_warehouse = customer_warehouse
                                            , customer_site = customer_site
                                            , customer_type = customer_type
                                            , customer_territory = customer_territory
                                            , customer_site_number = customer_site_number
                                            , customer_source = customer_source
                                            #  , customer_royalty_included = customer_royalty_included
                                            , customer_route_codes = customer_route_codes
                                            , customer_route_sequence = customer_route_sequence
                                            , customer_ship_via = customer_ship_via
                                            , customer_price_suffix = customer_price_suffix
                                            , customer_drop_ship = customer_drop_ship
                                            , customer_high_low_discount = customer_high_low_discount
                                            , customer_bill_to_name = customer_bill_to_name
                                            , customer_bill_to_street_1 = customer_bill_to_street_1
                                            #  , customer_bill_to_street_2 = customer_bill_to_street_2
                                            #  , customer_bill_to_street_3 = customer_bill_to_street_3
                                            #  , customer_bill_to_street_4 = customer_bill_to_street_4
                                            , customer_bill_to_city = customer_bill_to_city
                                            , customer_bill_to_state = customer_bill_to_state
                                            , customer_bill_to_zipcode = customer_bill_to_zipcode
                                            , customer_bill_to_country = customer_bill_to_country
                                            , customer_bill_to_phone = customer_bill_to_phone
                                            , customer_bill_to_fax = customer_bill_to_fax
                                            , customer_opened = customer_opened
                                            #  , customer_last_invoice = customer_last_invoice
                                            #  , customer_last_payment = customer_last_payment
                                            , customer_terms = customer_terms
                                            , customer_days = customer_days
                                            , customer_other = customer_other
                                            , customer_past_due_max = customer_past_due_max
                                            , customer_invoice_due_days = customer_invoice_due_days
                                            , customer_cod = customer_cod
                                            , customer_prepay_cc = customer_prepay_cc
                                            , customer_charge_freight = customer_charge_freight
                                            #  , customer_collector = customer_collector
                                            , customer_credit_hold_code = customer_credit_hold_code
                                            , customer_credit_limit = customer_credit_limit
                                            , customer_last_reviewed = customer_last_reviewed
                                            , customer_include_remakes = customer_include_remakes
                                            , customer_on_any_order_lower = customer_on_any_order_lower
                                            , customer_on_any_order_higher = customer_on_any_order_higher
                                            #  , customer_current_lower = customer_current_lower
                                            #  , customer_current_higher = customer_current_higher
                                            #  , customer_30_days_ar_lower = customer_30_days_ar_lower
                                            #  , customer_30_days_ar_higher = customer_30_days_ar_higher
                                            #  , customer_60_days_ar_lower = customer_60_days_ar_lower
                                            #  , customer_60_days_ar_higher = customer_60_days_ar_higher
                                            #  , customer_90_days_ar_lower = customer_90_days_ar_lower
                                            #  , customer_90_days_ar_higher = customer_90_days_ar_higher
                                            #  , customer_120_days_ar_lower = customer_120_days_ar_lower
                                            #  , customer_120_days_ar_higher = customer_120_days_ar_higher
                                            , customer_reference_1 = customer_reference_1
                                            , customer_waive_minimum_deposit = customer_waive_minimum_deposit
                                            #  , customer_reference_2 = customer_reference_2
                                            , customer_account_suspended = customer_account_suspended
                                            , customer_saleperson_1 = customer_saleperson_1
                                            #  , customer_saleperson_2 = customer_saleperson_2
                                            #  , customer_saleperson_3 = customer_saleperson_3
                                            #  , customer_saleperson_4 = customer_saleperson_4
                                            #  , customer_saleperson_5 = customer_saleperson_5
                                            #  , customer_constant_1 = customer_constant_1
                                            #  , customer_constant_2 = customer_constant_2
                                            #  , customer_constant_3 = customer_constant_3
                                            #  , customer_constant_4 = customer_constant_4
                                            #  , customer_constant_5 = customer_constant_5
                                            #  , customer_constant_6 = customer_constant_6
                                            #  , customer_constant_7 = customer_constant_7
                                            #  , customer_constant_8 = customer_constant_8
                                            #  , customer_constant_9 = customer_constant_9
                                            #  , customer_constant_10 = customer_constant_10
                                            #  , customer_constant_11 = customer_constant_11
                                            #  , customer_constant_12 = customer_constant_12
                                            #  , customer_constant_13 = customer_constant_13
                                            #  , customer_constant_14 = customer_constant_14
                                            #  , customer_constant_15 = customer_constant_15
                                            #  , customer_constant_16 = customer_constant_16
                                            #  , customer_constant_17 = customer_constant_17
                                            #  , customer_constant_18 = customer_constant_18
                                            #  , customer_constant_19 = customer_constant_19
                                            #  , customer_constant_20 = customer_constant_20
                                            #  , user_defined_1 = user_defined_1
                                            #  , user_defined_2 = user_defined_2
                                            #  , user_defined_3 = user_defined_3
                                            #  , user_defined_4 = user_defined_4
                                            #  , user_defined_5 = user_defined_5
                                            #  , user_defined_6 = user_defined_6
                                            #  , user_defined_7 = user_defined_7
                                            #  , user_defined_8 = user_defined_8
                                            #  , user_defined_9 = user_defined_9
                                            #  , user_defined_10 = user_defined_10
                                            #  , user_defined_11 = user_defined_11
                                            #  , user_defined_12 = user_defined_12
                                            #  , user_defined_13 = user_defined_13
                                            #  , user_defined_14 = user_defined_14
                                            #  , user_defined_15 = user_defined_15
                                            #  , user_defined_16 = user_defined_16
                                            #  , user_defined_17 = user_defined_17
                                            #  , user_defined_18 = user_defined_18
                                            #  , user_defined_19 = user_defined_19
                                            #  , user_defined_20 = user_defined_20
                                            , customer_customer_w_tax = customer_customer_w_tax
                                            , customer_limit_number_of_dealer_logins_to = customer_limit_number_of_dealer_logins_to
                                            , customer_days_to_hold_quotes = customer_days_to_hold_quotes
                                            #  , customer_enable_price_calculation = customer_enable_price_calculation
                                            #  , customer_enable_freight_calculation = customer_enable_freight_calculation
                                            #  , customer_collection_display = customer_collection_display
                                            #  , customer_internal_xml_id = customer_internal_xml_id
                                            #  , customer_client_quote_letter_verbiage = customer_client_quote_letter_verbiage
                                            #  , customer_booked_orders = customer_booked_orders
                                            #  , customer_deposits = customer_deposits
                                            #  , customer_balance_due = customer_balance_due
                                            #  , customer_open_ar = customer_open_ar
                                            #  , customer_30_day_ar = customer_30_day_ar
                                            #  , customer_60_day_ar = customer_60_day_ar
                                            #  , customer_90_day_ar = customer_90_day_ar
                                            #  , customer_120_day_ar = customer_120_day_ar
                                            #  , customer_unapplied = customer_unapplied
                                            #  , customer_total_open_ar = customer_total_open_ar
                                            #  , customer_ytd = customer_ytd
                                            #  , customer_previous_year = customer_previous_year
                                            #  , customer_high_sale = customer_high_sale
                                            #  , customer_py_high_sale = customer_py_high_sale
                                            #  , customer_cogs = customer_cogs
                                            #  , customer_py_cogs = customer_py_cogs
                                            , customer_avg_days_to_pay = customer_avg_days_to_pay
                                            , customer_pv_avg_days_to_pay = customer_pv_avg_days_to_pay
                                            , customer_times_past_due = customer_times_past_due
                                            , customer_py_times_past_due = customer_py_times_past_due

                                            , row_is_current = row_is_current, row_start_date = row_start_date, row_end_date = row_end_date
                                            , row_change_reason = row_change_reason
                                        )
                tran_customer.save()

        print(str(len(stage_customers))+' tran_customer update successful')
        # loading to datawarehouse tabel
        tran_customers = Tran_customer.objects.all()
        length = Tran_customer.objects.count()
        print(str(len(tran_customers)) + " customers in transform table")
        for i in range(0,len(tran_customers)):
            
            key = tran_customers[i].customer_account  
            if Dim_customer.objects.filter(customer_account=key).exists(): 

                dim_customer = Dim_customer.objects.filter(customer_account=key)

                customer_account = Tran_customer.objects.get(customer_account=key).customer_account
                customer_business_person = Tran_customer.objects.get(customer_account=key).customer_business_person
                customer_name = Tran_customer.objects.get(customer_account=key).customer_name
                customer_primary_phone = Tran_customer.objects.get(customer_account=key).customer_primary_phone
                customer_zip = Tran_customer.objects.get(customer_account=key).customer_zip
                customer_street_1 = Tran_customer.objects.get(customer_account=key).customer_street_1
                # customer_street_2 = Tran_customer.objects.get(customer_account=key).customer_street_2
                # customer_street_3 = Tran_customer.objects.get(customer_account=key).customer_street_3
                # customer_street_4 = Tran_customer.objects.get(customer_account=key).customer_street_4
                customer_city = Tran_customer.objects.get(customer_account=key).customer_city
                customer_state = Tran_customer.objects.get(customer_account=key).customer_state
                customer_country = Tran_customer.objects.get(customer_account=key).customer_country
                customer_address_type = Tran_customer.objects.get(customer_account=key).customer_address_type
                customer_address_fax = Tran_customer.objects.get(customer_account=key).customer_address_fax
                # customer_country_code = Tran_customer.objects.get(customer_account=key).customer_country_code
                # customer_idd_prefix = Tran_customer.objects.get(customer_account=key).customer_idd_prefix
                customer_account_activation_email = Tran_customer.objects.get(customer_account=key).customer_account_activation_email
                customer_advance_ship_notice = Tran_customer.objects.get(customer_account=key).customer_advance_ship_notice
                customer_order_submittal = Tran_customer.objects.get(customer_account=key).customer_order_submittal
                customer_email_subscription = Tran_customer.objects.get(customer_account=key).customer_email_subscription
                # customer_website = Tran_customer.objects.get(customer_account=key).customer_website
                # customer_customer_reference = Tran_customer.objects.get(customer_account=key).customer_customer_reference
                customer_default_order_comments = Tran_customer.objects.get(customer_account=key).customer_default_order_comments
                customer_default_invoice_comments = Tran_customer.objects.get(customer_account=key).customer_default_invoice_comments
                # customer_hide_cost_on_order_confirmation = Tran_customer.objects.get(customer_account=key).customer_hide_cost_on_order_confirmation
                # customer_allow_duplicate_po = Tran_customer.objects.get(customer_account=key).customer_allow_duplicate_po
                customer_first_name_last_name = Tran_customer.objects.get(customer_account=key).customer_first_name_last_name
                customer_work_phone = Tran_customer.objects.get(customer_account=key).customer_work_phone
                customer_ext = Tran_customer.objects.get(customer_account=key).customer_ext
                customer_cell_phone = Tran_customer.objects.get(customer_account=key).customer_cell_phone
                customer_home_phone = Tran_customer.objects.get(customer_account=key).customer_home_phone
                customer_fax = Tran_customer.objects.get(customer_account=key).customer_fax
                customer_corporate_account = Tran_customer.objects.get(customer_account=key).customer_corporate_account
                customer_email_credit_hold = Tran_customer.objects.get(customer_account=key).customer_email_credit_hold
                customer_credit_hold_email = Tran_customer.objects.get(customer_account=key).customer_credit_hold_email
                customer_art_hold_email = Tran_customer.objects.get(customer_account=key).customer_art_hold_email
                customer_email_invoice = Tran_customer.objects.get(customer_account=key).customer_email_invoice
                customer_invoice_notification = Tran_customer.objects.get(customer_account=key).customer_invoice_notification
                customer_email_invoice_past_due_alert = Tran_customer.objects.get(customer_account=key).customer_email_invoice_past_due_alert
                customer_invoice_past_due_alert = Tran_customer.objects.get(customer_account=key).customer_invoice_past_due_alert
                customer_email_statement = Tran_customer.objects.get(customer_account=key).customer_email_statement
                customer_statements = Tran_customer.objects.get(customer_account=key).customer_statements
                customer_email_credit_memo = Tran_customer.objects.get(customer_account=key).customer_email_credit_memo
                customer_credit_memo_email = Tran_customer.objects.get(customer_account=key).customer_credit_memo_email
                customer_email_return_reminder = Tran_customer.objects.get(customer_account=key).customer_email_return_reminder
                customer_return_reminder_email = Tran_customer.objects.get(customer_account=key).customer_return_reminder_email
                customer_reference_associate_email = Tran_customer.objects.get(customer_account=key).customer_reference_associate_email
                customer_fed_tax_code = Tran_customer.objects.get(customer_account=key).customer_fed_tax_code
                customer_fed_tax_freight = Tran_customer.objects.get(customer_account=key).customer_fed_tax_freight
                customer_fed_exempt_number = Tran_customer.objects.get(customer_account=key).customer_fed_exempt_number
                # customer_signed_fed_certificate = Tran_customer.objects.get(customer_account=key).customer_signed_fed_certificate
                customer_state_tax_code = Tran_customer.objects.get(customer_account=key).customer_state_tax_code
                customer_state_tax_freight = Tran_customer.objects.get(customer_account=key).customer_state_tax_freight
                customer_state_exempt_number = Tran_customer.objects.get(customer_account=key).customer_state_exempt_number
                # customer_signed_state_certificate = Tran_customer.objects.get(customer_account=key).customer_signed_state_certificate
                customer_warehouse = Tran_customer.objects.get(customer_account=key).customer_warehouse
                customer_site = Tran_customer.objects.get(customer_account=key).customer_site
                customer_type = Tran_customer.objects.get(customer_account=key).customer_type
                customer_territory = Tran_customer.objects.get(customer_account=key).customer_territory
                customer_site_number = Tran_customer.objects.get(customer_account=key).customer_site_number
                customer_source = Tran_customer.objects.get(customer_account=key).customer_source
                # customer_royalty_included = Tran_customer.objects.get(customer_account=key).customer_royalty_included
                customer_route_codes = Tran_customer.objects.get(customer_account=key).customer_route_codes
                customer_route_sequence = Tran_customer.objects.get(customer_account=key).customer_route_sequence
                customer_ship_via = Tran_customer.objects.get(customer_account=key).customer_ship_via
                customer_price_suffix = Tran_customer.objects.get(customer_account=key).customer_price_suffix
                customer_drop_ship = Tran_customer.objects.get(customer_account=key).customer_drop_ship
                customer_high_low_discount = Tran_customer.objects.get(customer_account=key).customer_high_low_discount
                customer_bill_to_name = Tran_customer.objects.get(customer_account=key).customer_bill_to_name
                customer_bill_to_street_1 = Tran_customer.objects.get(customer_account=key).customer_bill_to_street_1
                # customer_bill_to_street_2 = Tran_customer.objects.get(customer_account=key).customer_bill_to_street_2
                # customer_bill_to_street_3 = Tran_customer.objects.get(customer_account=key).customer_bill_to_street_3
                # customer_bill_to_street_4 = Tran_customer.objects.get(customer_account=key).customer_bill_to_street_4
                customer_bill_to_city = Tran_customer.objects.get(customer_account=key).customer_bill_to_city
                customer_bill_to_state = Tran_customer.objects.get(customer_account=key).customer_bill_to_state
                customer_bill_to_zipcode = Tran_customer.objects.get(customer_account=key).customer_bill_to_zipcode
                customer_bill_to_country = Tran_customer.objects.get(customer_account=key).customer_bill_to_country
                customer_bill_to_phone = Tran_customer.objects.get(customer_account=key).customer_bill_to_phone
                customer_bill_to_fax = Tran_customer.objects.get(customer_account=key).customer_bill_to_fax
                customer_opened = Tran_customer.objects.get(customer_account=key).customer_opened
                if customer_opened == "0000-00-00":
                    customer_opened = "2000-01-01"
                # customer_last_invoice = Tran_customer.objects.get(customer_account=key).customer_last_invoice
                # customer_last_payment = Tran_customer.objects.get(customer_account=key).customer_last_payment
                customer_terms = Tran_customer.objects.get(customer_account=key).customer_terms
                customer_days = Tran_customer.objects.get(customer_account=key).customer_days
                customer_other = Tran_customer.objects.get(customer_account=key).customer_other
                customer_past_due_max = Tran_customer.objects.get(customer_account=key).customer_past_due_max
                customer_invoice_due_days = Tran_customer.objects.get(customer_account=key).customer_invoice_due_days
                customer_cod = Tran_customer.objects.get(customer_account=key).customer_cod
                customer_prepay_cc = Tran_customer.objects.get(customer_account=key).customer_prepay_cc
                customer_charge_freight = Tran_customer.objects.get(customer_account=key).customer_charge_freight
                # customer_collector = Tran_customer.objects.get(customer_account=key).customer_collector
                customer_credit_hold_code = Tran_customer.objects.get(customer_account=key).customer_credit_hold_code
                customer_credit_limit = Tran_customer.objects.get(customer_account=key).customer_credit_limit
                customer_last_reviewed = Tran_customer.objects.get(customer_account=key).customer_last_reviewed
                customer_include_remakes = Tran_customer.objects.get(customer_account=key).customer_include_remakes
                customer_on_any_order_lower = Tran_customer.objects.get(customer_account=key).customer_on_any_order_lower
                customer_on_any_order_higher = Tran_customer.objects.get(customer_account=key).customer_on_any_order_higher
                # customer_current_lower = Tran_customer.objects.get(customer_account=key).customer_current_lower
                # customer_current_higher = Tran_customer.objects.get(customer_account=key).customer_current_higher
                # customer_30_days_ar_lower = Tran_customer.objects.get(customer_account=key).customer_30_days_ar_lower
                # customer_30_days_ar_higher = Tran_customer.objects.get(customer_account=key).customer_30_days_ar_higher
                # customer_60_days_ar_lower = Tran_customer.objects.get(customer_account=key).customer_60_days_ar_lower
                # customer_60_days_ar_higher = Tran_customer.objects.get(customer_account=key).customer_60_days_ar_higher
                # customer_90_days_ar_lower = Tran_customer.objects.get(customer_account=key).customer_90_days_ar_lower
                # customer_90_days_ar_higher = Tran_customer.objects.get(customer_account=key).customer_90_days_ar_higher
                # customer_120_days_ar_lower = Tran_customer.objects.get(customer_account=key).customer_120_days_ar_lower
                # customer_120_days_ar_higher = Tran_customer.objects.get(customer_account=key).customer_120_days_ar_higher
                customer_reference_1 = Tran_customer.objects.get(customer_account=key).customer_reference_1
                customer_waive_minimum_deposit = Tran_customer.objects.get(customer_account=key).customer_waive_minimum_deposit
                # customer_reference_2 = Tran_customer.objects.get(customer_account=key).customer_reference_2
                customer_account_suspended = Tran_customer.objects.get(customer_account=key).customer_account_suspended
                customer_saleperson_1 = Tran_customer.objects.get(customer_account=key).customer_saleperson_1
                # customer_saleperson_2 = Tran_customer.objects.get(customer_account=key).customer_saleperson_2
                # customer_saleperson_3 = Tran_customer.objects.get(customer_account=key).customer_saleperson_3
                # customer_saleperson_4 = Tran_customer.objects.get(customer_account=key).customer_saleperson_4
                # customer_saleperson_5 = Tran_customer.objects.get(customer_account=key).customer_saleperson_5
                # customer_constant_1 = Tran_customer.objects.get(customer_account=key).customer_constant_1
                # customer_constant_2 = Tran_customer.objects.get(customer_account=key).customer_constant_2
                # customer_constant_3 = Tran_customer.objects.get(customer_account=key).customer_constant_3
                # customer_constant_4 = Tran_customer.objects.get(customer_account=key).customer_constant_4
                # customer_constant_5 = Tran_customer.objects.get(customer_account=key).customer_constant_5
                # customer_constant_6 = Tran_customer.objects.get(customer_account=key).customer_constant_6
                # customer_constant_7 = Tran_customer.objects.get(customer_account=key).customer_constant_7
                # customer_constant_8 = Tran_customer.objects.get(customer_account=key).customer_constant_8
                # customer_constant_9 = Tran_customer.objects.get(customer_account=key).customer_constant_9
                # customer_constant_10 = Tran_customer.objects.get(customer_account=key).customer_constant_10
                # customer_constant_11 = Tran_customer.objects.get(customer_account=key).customer_constant_11
                # customer_constant_12 = Tran_customer.objects.get(customer_account=key).customer_constant_12
                # customer_constant_13 = Tran_customer.objects.get(customer_account=key).customer_constant_13
                # customer_constant_14 = Tran_customer.objects.get(customer_account=key).customer_constant_14
                # customer_constant_15 = Tran_customer.objects.get(customer_account=key).customer_constant_15
                # customer_constant_16 = Tran_customer.objects.get(customer_account=key).customer_constant_16
                # customer_constant_17 = Tran_customer.objects.get(customer_account=key).customer_constant_17
                # customer_constant_18 = Tran_customer.objects.get(customer_account=key).customer_constant_18
                # customer_constant_19 = Tran_customer.objects.get(customer_account=key).customer_constant_19
                # customer_constant_20 = Tran_customer.objects.get(customer_account=key).customer_constant_20
                # user_defined_1 = Tran_customer.objects.get(customer_account=key).user_defined_1
                # user_defined_2 = Tran_customer.objects.get(customer_account=key).user_defined_2
                # user_defined_3 = Tran_customer.objects.get(customer_account=key).user_defined_3
                # user_defined_4 = Tran_customer.objects.get(customer_account=key).user_defined_4
                # user_defined_5 = Tran_customer.objects.get(customer_account=key).user_defined_5
                # user_defined_6 = Tran_customer.objects.get(customer_account=key).user_defined_6
                # user_defined_7 = Tran_customer.objects.get(customer_account=key).user_defined_7
                # user_defined_8 = Tran_customer.objects.get(customer_account=key).user_defined_8
                # user_defined_9 = Tran_customer.objects.get(customer_account=key).user_defined_9
                # user_defined_10 = Tran_customer.objects.get(customer_account=key).user_defined_10
                # user_defined_11 = Tran_customer.objects.get(customer_account=key).user_defined_11
                # user_defined_12 = Tran_customer.objects.get(customer_account=key).user_defined_12
                # user_defined_13 = Tran_customer.objects.get(customer_account=key).user_defined_13
                # user_defined_14 = Tran_customer.objects.get(customer_account=key).user_defined_14
                # user_defined_15 = Tran_customer.objects.get(customer_account=key).user_defined_15
                # user_defined_16 = Tran_customer.objects.get(customer_account=key).user_defined_16
                # user_defined_17 = Tran_customer.objects.get(customer_account=key).user_defined_17
                # user_defined_18 = Tran_customer.objects.get(customer_account=key).user_defined_18
                # user_defined_19 = Tran_customer.objects.get(customer_account=key).user_defined_19
                # user_defined_20 = Tran_customer.objects.get(customer_account=key).user_defined_20
                customer_customer_w_tax = Tran_customer.objects.get(customer_account=key).customer_customer_w_tax
                customer_limit_number_of_dealer_logins_to = Tran_customer.objects.get(customer_account=key).customer_limit_number_of_dealer_logins_to
                customer_days_to_hold_quotes = Tran_customer.objects.get(customer_account=key).customer_days_to_hold_quotes
                # customer_enable_price_calculation = Tran_customer.objects.get(customer_account=key).customer_enable_price_calculation
                # customer_enable_freight_calculation = Tran_customer.objects.get(customer_account=key).customer_enable_freight_calculation
                # customer_collection_display = Tran_customer.objects.get(customer_account=key).customer_collection_display
                # customer_internal_xml_id = Tran_customer.objects.get(customer_account=key).customer_internal_xml_id
                # customer_client_quote_letter_verbiage = Tran_customer.objects.get(customer_account=key).customer_client_quote_letter_verbiage
                # customer_booked_orders = Tran_customer.objects.get(customer_account=key).customer_booked_orders
                # customer_deposits = Tran_customer.objects.get(customer_account=key).customer_deposits
                # customer_balance_due = Tran_customer.objects.get(customer_account=key).customer_balance_due
                # customer_open_ar = Tran_customer.objects.get(customer_account=key).customer_open_ar
                # customer_30_day_ar = Tran_customer.objects.get(customer_account=key).customer_30_day_ar
                # customer_60_day_ar = Tran_customer.objects.get(customer_account=key).customer_60_day_ar
                # customer_90_day_ar = Tran_customer.objects.get(customer_account=key).customer_90_day_ar
                # customer_120_day_ar = Tran_customer.objects.get(customer_account=key).customer_120_day_ar
                # customer_unapplied = Tran_customer.objects.get(customer_account=key).customer_unapplied
                # customer_total_open_ar = Tran_customer.objects.get(customer_account=key).customer_total_open_ar
                # customer_ytd = Tran_customer.objects.get(customer_account=key).customer_ytd
                # customer_previous_year = Tran_customer.objects.get(customer_account=key).customer_previous_year
                # customer_high_sale = Tran_customer.objects.get(customer_account=key).customer_high_sale
                # customer_py_high_sale = Tran_customer.objects.get(customer_account=key).customer_py_high_sale
                # customer_cogs = Tran_customer.objects.get(customer_account=key).customer_cogs
                # customer_py_cogs = Tran_customer.objects.get(customer_account=key).customer_py_cogs
                customer_avg_days_to_pay = Tran_customer.objects.get(customer_account=key).customer_avg_days_to_pay
                customer_pv_avg_days_to_pay = Tran_customer.objects.get(customer_account=key).customer_pv_avg_days_to_pay
                customer_times_past_due = Tran_customer.objects.get(customer_account=key).customer_times_past_due
                customer_py_times_past_due = Tran_customer.objects.get(customer_account=key).customer_py_times_past_due

                row_is_current = Tran_customer.objects.get(customer_account=key).row_is_current
                row_end_date = Tran_customer.objects.get(customer_account=key).row_end_date
                row_change_reason = "normal update"

                dim_customer.update(
                                  customer_account=customer_account
                                , customer_business_person=customer_business_person
                                , customer_name= customer_name
                                , customer_primary_phone = customer_primary_phone
                                , customer_zip = customer_zip
                                , customer_street_1 = customer_street_1
                                #  , customer_street_2 = customer_street_2
                                #  , customer_street_3 = customer_street_3
                                #  , customer_street_4 = customer_street_4
                                , customer_city = customer_city
                                , customer_state = customer_state
                                , customer_country = customer_country
                                , customer_address_type = customer_address_type
                                , customer_address_fax = customer_address_fax
                                #  , customer_country_code = customer_country_code
                                #  , customer_idd_prefix = customer_idd_prefix
                                , customer_account_activation_email = customer_account_activation_email
                                , customer_advance_ship_notice = customer_advance_ship_notice
                                , customer_order_submittal = customer_order_submittal
                                , customer_email_subscription = customer_email_subscription
                                #  , customer_website = customer_website
                                #  , customer_customer_reference = customer_customer_reference
                                , customer_default_order_comments = customer_default_order_comments
                                , customer_default_invoice_comments = customer_default_invoice_comments
                                #  , customer_hide_cost_on_order_confirmation = customer_hide_cost_on_order_confirmation
                                #  , customer_allow_duplicate_po = customer_allow_duplicate_po
                                , customer_first_name_last_name = customer_first_name_last_name
                                , customer_work_phone = customer_work_phone
                                , customer_ext = customer_ext
                                , customer_cell_phone = customer_cell_phone
                                , customer_home_phone = customer_home_phone
                                , customer_fax = customer_fax
                                , customer_corporate_account = customer_corporate_account
                                , customer_email_credit_hold = customer_email_credit_hold
                                , customer_credit_hold_email = customer_credit_hold_email
                                , customer_art_hold_email = customer_art_hold_email
                                , customer_email_invoice = customer_email_invoice
                                , customer_invoice_notification = customer_invoice_notification
                                , customer_email_invoice_past_due_alert = customer_email_invoice_past_due_alert
                                , customer_invoice_past_due_alert = customer_invoice_past_due_alert
                                , customer_email_statement = customer_email_statement
                                , customer_statements = customer_statements
                                , customer_email_credit_memo = customer_email_credit_memo
                                , customer_credit_memo_email = customer_credit_memo_email
                                , customer_email_return_reminder = customer_email_return_reminder
                                , customer_return_reminder_email = customer_return_reminder_email
                                , customer_reference_associate_email = customer_reference_associate_email
                                , customer_fed_tax_code = customer_fed_tax_code
                                , customer_fed_tax_freight = customer_fed_tax_freight
                                , customer_fed_exempt_number = customer_fed_exempt_number
                                #  , customer_signed_fed_certificate = customer_signed_fed_certificate
                                , customer_state_tax_code = customer_state_tax_code
                                , customer_state_tax_freight = customer_state_tax_freight
                                , customer_state_exempt_number = customer_state_exempt_number
                                #  , customer_signed_state_certificate = customer_signed_state_certificate
                                , customer_warehouse = customer_warehouse
                                , customer_site = customer_site
                                , customer_type = customer_type
                                , customer_territory = customer_territory
                                , customer_site_number = customer_site_number
                                , customer_source = customer_source
                                #  , customer_royalty_included = customer_royalty_included
                                , customer_route_codes = customer_route_codes
                                , customer_route_sequence = customer_route_sequence
                                , customer_ship_via = customer_ship_via
                                , customer_price_suffix = customer_price_suffix
                                , customer_drop_ship = customer_drop_ship
                                , customer_high_low_discount = customer_high_low_discount
                                , customer_bill_to_name = customer_bill_to_name
                                , customer_bill_to_street_1 = customer_bill_to_street_1
                                #  , customer_bill_to_street_2 = customer_bill_to_street_2
                                #  , customer_bill_to_street_3 = customer_bill_to_street_3
                                #  , customer_bill_to_street_4 = customer_bill_to_street_4
                                , customer_bill_to_city = customer_bill_to_city
                                , customer_bill_to_state = customer_bill_to_state
                                , customer_bill_to_zipcode = customer_bill_to_zipcode
                                , customer_bill_to_country = customer_bill_to_country
                                , customer_bill_to_phone = customer_bill_to_phone
                                , customer_bill_to_fax = customer_bill_to_fax
                                , customer_opened = customer_opened
                                #  , customer_last_invoice = customer_last_invoice
                                #  , customer_last_payment = customer_last_payment
                                , customer_terms = customer_terms
                                , customer_days = customer_days
                                , customer_other = customer_other
                                , customer_past_due_max = customer_past_due_max
                                , customer_invoice_due_days = customer_invoice_due_days
                                , customer_cod = customer_cod
                                , customer_prepay_cc = customer_prepay_cc
                                , customer_charge_freight = customer_charge_freight
                                #  , customer_collector = customer_collector
                                , customer_credit_hold_code = customer_credit_hold_code
                                , customer_credit_limit = customer_credit_limit
                                , customer_last_reviewed = customer_last_reviewed
                                , customer_include_remakes = customer_include_remakes
                                , customer_on_any_order_lower = customer_on_any_order_lower
                                , customer_on_any_order_higher = customer_on_any_order_higher
                                #  , customer_current_lower = customer_current_lower
                                #  , customer_current_higher = customer_current_higher
                                #  , customer_30_days_ar_lower = customer_30_days_ar_lower
                                #  , customer_30_days_ar_higher = customer_30_days_ar_higher
                                #  , customer_60_days_ar_lower = customer_60_days_ar_lower
                                #  , customer_60_days_ar_higher = customer_60_days_ar_higher
                                #  , customer_90_days_ar_lower = customer_90_days_ar_lower
                                #  , customer_90_days_ar_higher = customer_90_days_ar_higher
                                #  , customer_120_days_ar_lower = customer_120_days_ar_lower
                                #  , customer_120_days_ar_higher = customer_120_days_ar_higher
                                , customer_reference_1 = customer_reference_1
                                , customer_waive_minimum_deposit = customer_waive_minimum_deposit
                                #  , customer_reference_2 = customer_reference_2
                                , customer_account_suspended = customer_account_suspended
                                , customer_saleperson_1 = customer_saleperson_1
                                #  , customer_saleperson_2 = customer_saleperson_2
                                #  , customer_saleperson_3 = customer_saleperson_3
                                #  , customer_saleperson_4 = customer_saleperson_4
                                #  , customer_saleperson_5 = customer_saleperson_5
                                #  , customer_constant_1 = customer_constant_1
                                #  , customer_constant_2 = customer_constant_2
                                #  , customer_constant_3 = customer_constant_3
                                #  , customer_constant_4 = customer_constant_4
                                #  , customer_constant_5 = customer_constant_5
                                #  , customer_constant_6 = customer_constant_6
                                #  , customer_constant_7 = customer_constant_7
                                #  , customer_constant_8 = customer_constant_8
                                #  , customer_constant_9 = customer_constant_9
                                #  , customer_constant_10 = customer_constant_10
                                #  , customer_constant_11 = customer_constant_11
                                #  , customer_constant_12 = customer_constant_12
                                #  , customer_constant_13 = customer_constant_13
                                #  , customer_constant_14 = customer_constant_14
                                #  , customer_constant_15 = customer_constant_15
                                #  , customer_constant_16 = customer_constant_16
                                #  , customer_constant_17 = customer_constant_17
                                #  , customer_constant_18 = customer_constant_18
                                #  , customer_constant_19 = customer_constant_19
                                #  , customer_constant_20 = customer_constant_20
                                #  , user_defined_1 = user_defined_1
                                #  , user_defined_2 = user_defined_2
                                #  , user_defined_3 = user_defined_3
                                #  , user_defined_4 = user_defined_4
                                #  , user_defined_5 = user_defined_5
                                #  , user_defined_6 = user_defined_6
                                #  , user_defined_7 = user_defined_7
                                #  , user_defined_8 = user_defined_8
                                #  , user_defined_9 = user_defined_9
                                #  , user_defined_10 = user_defined_10
                                #  , user_defined_11 = user_defined_11
                                #  , user_defined_12 = user_defined_12
                                #  , user_defined_13 = user_defined_13
                                #  , user_defined_14 = user_defined_14
                                #  , user_defined_15 = user_defined_15
                                #  , user_defined_16 = user_defined_16
                                #  , user_defined_17 = user_defined_17
                                #  , user_defined_18 = user_defined_18
                                #  , user_defined_19 = user_defined_19
                                #  , user_defined_20 = user_defined_20
                                , customer_customer_w_tax = customer_customer_w_tax
                                , customer_limit_number_of_dealer_logins_to = customer_limit_number_of_dealer_logins_to
                                , customer_days_to_hold_quotes = customer_days_to_hold_quotes
                                #  , customer_enable_price_calculation = customer_enable_price_calculation
                                #  , customer_enable_freight_calculation = customer_enable_freight_calculation
                                #  , customer_collection_display = customer_collection_display
                                #  , customer_internal_xml_id = customer_internal_xml_id
                                #  , customer_client_quote_letter_verbiage = customer_client_quote_letter_verbiage
                                #  , customer_booked_orders = customer_booked_orders
                                #  , customer_deposits = customer_deposits
                                #  , customer_balance_due = customer_balance_due
                                #  , customer_open_ar = customer_open_ar
                                #  , customer_30_day_ar = customer_30_day_ar
                                #  , customer_60_day_ar = customer_60_day_ar
                                #  , customer_90_day_ar = customer_90_day_ar
                                #  , customer_120_day_ar = customer_120_day_ar
                                #  , customer_unapplied = customer_unapplied
                                #  , customer_total_open_ar = customer_total_open_ar
                                #  , customer_ytd = customer_ytd
                                #  , customer_previous_year = customer_previous_year
                                #  , customer_high_sale = customer_high_sale
                                #  , customer_py_high_sale = customer_py_high_sale
                                #  , customer_cogs = customer_cogs
                                #  , customer_py_cogs = customer_py_cogs
                                , customer_avg_days_to_pay = customer_avg_days_to_pay
                                , customer_pv_avg_days_to_pay = customer_pv_avg_days_to_pay
                                , customer_times_past_due = customer_times_past_due
                                , customer_py_times_past_due = customer_py_times_past_due
                            
                                , row_is_current = row_is_current, row_end_date = row_end_date, row_change_reason = row_change_reason)

                #messages.success(request, 'Form successfully submitted') # Any message you wish
            
            else:
                customer_account = tran_customers[i].customer_account
                customer_business_person = tran_customers[i].customer_business_person
                customer_name = tran_customers[i].customer_name
                customer_primary_phone = tran_customers[i].customer_primary_phone
                customer_zip = tran_customers[i].customer_zip
                customer_street_1 = tran_customers[i].customer_street_1
                # customer_street_2 = tran_customers[i].customer_street_2
                # customer_street_3 = tran_customers[i].customer_street_3
                # customer_street_4 = tran_customers[i].customer_street_4
                customer_city = tran_customers[i].customer_city
                customer_state = tran_customers[i].customer_state
                customer_country = tran_customers[i].customer_country
                customer_address_type = tran_customers[i].customer_address_type
                customer_address_fax = tran_customers[i].customer_address_fax
                # customer_country_code = tran_customers[i].customer_country_code
                # customer_idd_prefix = tran_customers[i].customer_idd_prefix
                customer_account_activation_email = tran_customers[i].customer_account_activation_email
                customer_advance_ship_notice = tran_customers[i].customer_advance_ship_notice
                customer_order_submittal = tran_customers[i].customer_order_submittal
                customer_email_subscription = tran_customers[i].customer_email_subscription
                # customer_website = tran_customers[i].customer_website
                # customer_customer_reference = tran_customers[i].customer_customer_reference
                customer_default_order_comments = tran_customers[i].customer_default_order_comments
                customer_default_invoice_comments = tran_customers[i].customer_default_invoice_comments
                # customer_hide_cost_on_order_confirmation = tran_customers[i].customer_hide_cost_on_order_confirmation
                # customer_allow_duplicate_po = tran_customers[i].customer_allow_duplicate_po
                customer_first_name_last_name = tran_customers[i].customer_first_name_last_name
                customer_work_phone = tran_customers[i].customer_work_phone
                customer_ext = tran_customers[i].customer_ext
                customer_cell_phone = tran_customers[i].customer_cell_phone
                customer_home_phone = tran_customers[i].customer_home_phone
                customer_fax = tran_customers[i].customer_fax
                customer_corporate_account = tran_customers[i].customer_corporate_account
                customer_email_credit_hold = tran_customers[i].customer_email_credit_hold
                customer_credit_hold_email = tran_customers[i].customer_credit_hold_email
                customer_art_hold_email = tran_customers[i].customer_art_hold_email
                customer_email_invoice = tran_customers[i].customer_email_invoice
                customer_invoice_notification = tran_customers[i].customer_invoice_notification
                customer_email_invoice_past_due_alert = tran_customers[i].customer_email_invoice_past_due_alert
                customer_invoice_past_due_alert = tran_customers[i].customer_invoice_past_due_alert
                customer_email_statement = tran_customers[i].customer_email_statement
                customer_statements = tran_customers[i].customer_statements
                customer_email_credit_memo = tran_customers[i].customer_email_credit_memo
                customer_credit_memo_email = tran_customers[i].customer_credit_memo_email
                customer_email_return_reminder = tran_customers[i].customer_email_return_reminder
                customer_return_reminder_email = tran_customers[i].customer_return_reminder_email
                customer_reference_associate_email = tran_customers[i].customer_reference_associate_email
                customer_fed_tax_code = tran_customers[i].customer_fed_tax_code
                customer_fed_tax_freight = tran_customers[i].customer_fed_tax_freight
                customer_fed_exempt_number = tran_customers[i].customer_fed_exempt_number
                # customer_signed_fed_certificate = tran_customers[i].customer_signed_fed_certificate
                customer_state_tax_code = tran_customers[i].customer_state_tax_code
                customer_state_tax_freight = tran_customers[i].customer_state_tax_freight
                customer_state_exempt_number = tran_customers[i].customer_state_exempt_number
                # customer_signed_state_certificate = tran_customers[i].customer_signed_state_certificate
                customer_warehouse = tran_customers[i].customer_warehouse
                customer_site = tran_customers[i].customer_site
                customer_type = tran_customers[i].customer_type
                customer_territory = tran_customers[i].customer_territory
                customer_site_number = tran_customers[i].customer_site_number
                customer_source = tran_customers[i].customer_source
                # customer_royalty_included = tran_customers[i].customer_royalty_included
                customer_route_codes = tran_customers[i].customer_route_codes
                customer_route_sequence = tran_customers[i].customer_route_sequence
                customer_ship_via = tran_customers[i].customer_ship_via
                customer_price_suffix = tran_customers[i].customer_price_suffix
                customer_drop_ship = tran_customers[i].customer_drop_ship
                customer_high_low_discount = tran_customers[i].customer_high_low_discount
                customer_bill_to_name = tran_customers[i].customer_bill_to_name
                customer_bill_to_street_1 = tran_customers[i].customer_bill_to_street_1
                # customer_bill_to_street_2 = tran_customers[i].customer_bill_to_street_2
                # customer_bill_to_street_3 = tran_customers[i].customer_bill_to_street_3
                # customer_bill_to_street_4 = tran_customers[i].customer_bill_to_street_4
                customer_bill_to_city = tran_customers[i].customer_bill_to_city
                customer_bill_to_state = tran_customers[i].customer_bill_to_state
                customer_bill_to_zipcode = tran_customers[i].customer_bill_to_zipcode
                customer_bill_to_country = tran_customers[i].customer_bill_to_country
                customer_bill_to_phone = tran_customers[i].customer_bill_to_phone
                customer_bill_to_fax = tran_customers[i].customer_bill_to_fax
                customer_opened = tran_customers[i].customer_opened
                # customer_last_invoice = tran_customers[i].customer_last_invoice
                # customer_last_payment = tran_customers[i].customer_last_payment
                customer_terms = tran_customers[i].customer_terms
                customer_days = tran_customers[i].customer_days
                customer_other = tran_customers[i].customer_other
                customer_past_due_max = tran_customers[i].customer_past_due_max
                customer_invoice_due_days = tran_customers[i].customer_invoice_due_days
                customer_cod = tran_customers[i].customer_cod
                customer_prepay_cc = tran_customers[i].customer_prepay_cc
                customer_charge_freight = tran_customers[i].customer_charge_freight
                # customer_collector = tran_customers[i].customer_collector
                customer_credit_hold_code = tran_customers[i].customer_credit_hold_code
                customer_credit_limit = tran_customers[i].customer_credit_limit
                customer_last_reviewed = tran_customers[i].customer_last_reviewed
                customer_include_remakes = tran_customers[i].customer_include_remakes
                customer_on_any_order_lower = tran_customers[i].customer_on_any_order_lower
                customer_on_any_order_higher = tran_customers[i].customer_on_any_order_higher
                # customer_current_lower = tran_customers[i].customer_current_lower
                # customer_current_higher = tran_customers[i].customer_current_higher
                # customer_30_days_ar_lower = tran_customers[i].customer_30_days_ar_lower
                # customer_30_days_ar_higher = tran_customers[i].customer_30_days_ar_higher
                # customer_60_days_ar_lower = tran_customers[i].customer_60_days_ar_lower
                # customer_60_days_ar_higher = tran_customers[i].customer_60_days_ar_higher
                # customer_90_days_ar_lower = tran_customers[i].customer_90_days_ar_lower
                # customer_90_days_ar_higher = tran_customers[i].customer_90_days_ar_higher
                # customer_120_days_ar_lower = tran_customers[i].customer_120_days_ar_lower
                # customer_120_days_ar_higher = tran_customers[i].customer_120_days_ar_higher
                customer_reference_1 = tran_customers[i].customer_reference_1
                customer_waive_minimum_deposit = tran_customers[i].customer_waive_minimum_deposit
                # customer_reference_2 = tran_customers[i].customer_reference_2
                customer_account_suspended = tran_customers[i].customer_account_suspended
                customer_saleperson_1 = tran_customers[i].customer_saleperson_1
                # customer_saleperson_2 = tran_customers[i].customer_saleperson_2
                # customer_saleperson_3 = tran_customers[i].customer_saleperson_3
                # customer_saleperson_4 = tran_customers[i].customer_saleperson_4
                # customer_saleperson_5 = tran_customers[i].customer_saleperson_5
                # customer_constant_1 = tran_customers[i].customer_constant_1
                # customer_constant_2 = tran_customers[i].customer_constant_2
                # customer_constant_3 = tran_customers[i].customer_constant_3
                # customer_constant_4 = tran_customers[i].customer_constant_4
                # customer_constant_5 = tran_customers[i].customer_constant_5
                # customer_constant_6 = tran_customers[i].customer_constant_6
                # customer_constant_7 = tran_customers[i].customer_constant_7
                # customer_constant_8 = tran_customers[i].customer_constant_8
                # customer_constant_9 = tran_customers[i].customer_constant_9
                # customer_constant_10 = tran_customers[i].customer_constant_10
                # customer_constant_11 = tran_customers[i].customer_constant_11
                # customer_constant_12 = tran_customers[i].customer_constant_12
                # customer_constant_13 = tran_customers[i].customer_constant_13
                # customer_constant_14 = tran_customers[i].customer_constant_14
                # customer_constant_15 = tran_customers[i].customer_constant_15
                # customer_constant_16 = tran_customers[i].customer_constant_16
                # customer_constant_17 = tran_customers[i].customer_constant_17
                # customer_constant_18 = tran_customers[i].customer_constant_18
                # customer_constant_19 = tran_customers[i].customer_constant_19
                # customer_constant_20 = tran_customers[i].customer_constant_20
                # user_defined_1 = tran_customers[i].user_defined_1
                # user_defined_2 = tran_customers[i].user_defined_2
                # user_defined_3 = tran_customers[i].user_defined_3
                # user_defined_4 = tran_customers[i].user_defined_4
                # user_defined_5 = tran_customers[i].user_defined_5
                # user_defined_6 = tran_customers[i].user_defined_6
                # user_defined_7 = tran_customers[i].user_defined_7
                # user_defined_8 = tran_customers[i].user_defined_8
                # user_defined_9 = tran_customers[i].user_defined_9
                # user_defined_10 = tran_customers[i].user_defined_10
                # user_defined_11 = tran_customers[i].user_defined_11
                # user_defined_12 = tran_customers[i].user_defined_12
                # user_defined_13 = tran_customers[i].user_defined_13
                # user_defined_14 = tran_customers[i].user_defined_14
                # user_defined_15 = tran_customers[i].user_defined_15
                # user_defined_16 = tran_customers[i].user_defined_16
                # user_defined_17 = tran_customers[i].user_defined_17
                # user_defined_18 = tran_customers[i].user_defined_18
                # user_defined_19 = tran_customers[i].user_defined_19
                # user_defined_20 = tran_customers[i].user_defined_20
                customer_customer_w_tax = tran_customers[i].customer_customer_w_tax
                customer_limit_number_of_dealer_logins_to = tran_customers[i].customer_limit_number_of_dealer_logins_to
                customer_days_to_hold_quotes = tran_customers[i].customer_days_to_hold_quotes
                # customer_enable_price_calculation = tran_customers[i].customer_enable_price_calculation
                # customer_enable_freight_calculation = tran_customers[i].customer_enable_freight_calculation
                # customer_collection_display = tran_customers[i].customer_collection_display
                # customer_internal_xml_id = tran_customers[i].customer_internal_xml_id
                # customer_client_quote_letter_verbiage = tran_customers[i].customer_client_quote_letter_verbiage
                # customer_booked_orders = tran_customers[i].customer_booked_orders
                # customer_deposits = tran_customers[i].customer_deposits
                # customer_balance_due = tran_customers[i].customer_balance_due
                # customer_open_ar = tran_customers[i].customer_open_ar
                # customer_30_day_ar = tran_customers[i].customer_30_day_ar
                # customer_60_day_ar = tran_customers[i].customer_60_day_ar
                # customer_90_day_ar = tran_customers[i].customer_90_day_ar
                # customer_120_day_ar = tran_customers[i].customer_120_day_ar
                # customer_unapplied = tran_customers[i].customer_unapplied
                # customer_total_open_ar = tran_customers[i].customer_total_open_ar
                # customer_ytd = tran_customers[i].customer_ytd
                # customer_previous_year = tran_customers[i].customer_previous_year
                # customer_high_sale = tran_customers[i].customer_high_sale
                # customer_py_high_sale = tran_customers[i].customer_py_high_sale
                # customer_cogs = tran_customers[i].customer_cogs
                # customer_py_cogs = tran_customers[i].customer_py_cogs
                customer_avg_days_to_pay = tran_customers[i].customer_avg_days_to_pay
                customer_pv_avg_days_to_pay = tran_customers[i].customer_pv_avg_days_to_pay
                customer_times_past_due = tran_customers[i].customer_times_past_due
                customer_py_times_past_due = tran_customers[i].customer_py_times_past_due

                row_is_current = tran_customers[i].row_is_current
                row_start_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_end_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row_change_reason = "original state"

                dim_customer = Dim_customer(
                                          customer_account=customer_account
                                        , customer_business_person=customer_business_person
                                        , customer_name= customer_name
                                        , customer_primary_phone = customer_primary_phone
                                        , customer_zip = customer_zip
                                        , customer_street_1 = customer_street_1
                                        #  , customer_street_2 = customer_street_2
                                        #  , customer_street_3 = customer_street_3
                                        #  , customer_street_4 = customer_street_4
                                        , customer_city = customer_city
                                        , customer_state = customer_state
                                        , customer_country = customer_country
                                        , customer_address_type = customer_address_type
                                        , customer_address_fax = customer_address_fax
                                        #  , customer_country_code = customer_country_code
                                        #  , customer_idd_prefix = customer_idd_prefix
                                        , customer_account_activation_email = customer_account_activation_email
                                        , customer_advance_ship_notice = customer_advance_ship_notice
                                        , customer_order_submittal = customer_order_submittal
                                        , customer_email_subscription = customer_email_subscription
                                        #  , customer_website = customer_website
                                        #  , customer_customer_reference = customer_customer_reference
                                        , customer_default_order_comments = customer_default_order_comments
                                        , customer_default_invoice_comments = customer_default_invoice_comments
                                        #  , customer_hide_cost_on_order_confirmation = customer_hide_cost_on_order_confirmation
                                        #  , customer_allow_duplicate_po = customer_allow_duplicate_po
                                        , customer_first_name_last_name = customer_first_name_last_name
                                        , customer_work_phone = customer_work_phone
                                        , customer_ext = customer_ext
                                        , customer_cell_phone = customer_cell_phone
                                        , customer_home_phone = customer_home_phone
                                        , customer_fax = customer_fax
                                        , customer_corporate_account = customer_corporate_account
                                        , customer_email_credit_hold = customer_email_credit_hold
                                        , customer_credit_hold_email = customer_credit_hold_email
                                        , customer_art_hold_email = customer_art_hold_email
                                        , customer_email_invoice = customer_email_invoice
                                        , customer_invoice_notification = customer_invoice_notification
                                        , customer_email_invoice_past_due_alert = customer_email_invoice_past_due_alert
                                        , customer_invoice_past_due_alert = customer_invoice_past_due_alert
                                        , customer_email_statement = customer_email_statement
                                        , customer_statements = customer_statements
                                        , customer_email_credit_memo = customer_email_credit_memo
                                        , customer_credit_memo_email = customer_credit_memo_email
                                        , customer_email_return_reminder = customer_email_return_reminder
                                        , customer_return_reminder_email = customer_return_reminder_email
                                        , customer_reference_associate_email = customer_reference_associate_email
                                        , customer_fed_tax_code = customer_fed_tax_code
                                        , customer_fed_tax_freight = customer_fed_tax_freight
                                        , customer_fed_exempt_number = customer_fed_exempt_number
                                        #  , customer_signed_fed_certificate = customer_signed_fed_certificate
                                        , customer_state_tax_code = customer_state_tax_code
                                        , customer_state_tax_freight = customer_state_tax_freight
                                        , customer_state_exempt_number = customer_state_exempt_number
                                        #  , customer_signed_state_certificate = customer_signed_state_certificate
                                        , customer_warehouse = customer_warehouse
                                        , customer_site = customer_site
                                        , customer_type = customer_type
                                        , customer_territory = customer_territory
                                        , customer_site_number = customer_site_number
                                        , customer_source = customer_source
                                        #  , customer_royalty_included = customer_royalty_included
                                        , customer_route_codes = customer_route_codes
                                        , customer_route_sequence = customer_route_sequence
                                        , customer_ship_via = customer_ship_via
                                        , customer_price_suffix = customer_price_suffix
                                        , customer_drop_ship = customer_drop_ship
                                        , customer_high_low_discount = customer_high_low_discount
                                        , customer_bill_to_name = customer_bill_to_name
                                        , customer_bill_to_street_1 = customer_bill_to_street_1
                                        #  , customer_bill_to_street_2 = customer_bill_to_street_2
                                        #  , customer_bill_to_street_3 = customer_bill_to_street_3
                                        #  , customer_bill_to_street_4 = customer_bill_to_street_4
                                        , customer_bill_to_city = customer_bill_to_city
                                        , customer_bill_to_state = customer_bill_to_state
                                        , customer_bill_to_zipcode = customer_bill_to_zipcode
                                        , customer_bill_to_country = customer_bill_to_country
                                        , customer_bill_to_phone = customer_bill_to_phone
                                        , customer_bill_to_fax = customer_bill_to_fax
                                        , customer_opened = customer_opened
                                        #  , customer_last_invoice = customer_last_invoice
                                        #  , customer_last_payment = customer_last_payment
                                        , customer_terms = customer_terms
                                        , customer_days = customer_days
                                        , customer_other = customer_other
                                        , customer_past_due_max = customer_past_due_max
                                        , customer_invoice_due_days = customer_invoice_due_days
                                        , customer_cod = customer_cod
                                        , customer_prepay_cc = customer_prepay_cc
                                        , customer_charge_freight = customer_charge_freight
                                        #  , customer_collector = customer_collector
                                        , customer_credit_hold_code = customer_credit_hold_code
                                        , customer_credit_limit = customer_credit_limit
                                        , customer_last_reviewed = customer_last_reviewed
                                        , customer_include_remakes = customer_include_remakes
                                        , customer_on_any_order_lower = customer_on_any_order_lower
                                        , customer_on_any_order_higher = customer_on_any_order_higher
                                        #  , customer_current_lower = customer_current_lower
                                        #  , customer_current_higher = customer_current_higher
                                        #  , customer_30_days_ar_lower = customer_30_days_ar_lower
                                        #  , customer_30_days_ar_higher = customer_30_days_ar_higher
                                        #  , customer_60_days_ar_lower = customer_60_days_ar_lower
                                        #  , customer_60_days_ar_higher = customer_60_days_ar_higher
                                        #  , customer_90_days_ar_lower = customer_90_days_ar_lower
                                        #  , customer_90_days_ar_higher = customer_90_days_ar_higher
                                        #  , customer_120_days_ar_lower = customer_120_days_ar_lower
                                        #  , customer_120_days_ar_higher = customer_120_days_ar_higher
                                        , customer_reference_1 = customer_reference_1
                                        , customer_waive_minimum_deposit = customer_waive_minimum_deposit
                                        #  , customer_reference_2 = customer_reference_2
                                        , customer_account_suspended = customer_account_suspended
                                        , customer_saleperson_1 = customer_saleperson_1
                                        #  , customer_saleperson_2 = customer_saleperson_2
                                        #  , customer_saleperson_3 = customer_saleperson_3
                                        #  , customer_saleperson_4 = customer_saleperson_4
                                        #  , customer_saleperson_5 = customer_saleperson_5
                                        #  , customer_constant_1 = customer_constant_1
                                        #  , customer_constant_2 = customer_constant_2
                                        #  , customer_constant_3 = customer_constant_3
                                        #  , customer_constant_4 = customer_constant_4
                                        #  , customer_constant_5 = customer_constant_5
                                        #  , customer_constant_6 = customer_constant_6
                                        #  , customer_constant_7 = customer_constant_7
                                        #  , customer_constant_8 = customer_constant_8
                                        #  , customer_constant_9 = customer_constant_9
                                        #  , customer_constant_10 = customer_constant_10
                                        #  , customer_constant_11 = customer_constant_11
                                        #  , customer_constant_12 = customer_constant_12
                                        #  , customer_constant_13 = customer_constant_13
                                        #  , customer_constant_14 = customer_constant_14
                                        #  , customer_constant_15 = customer_constant_15
                                        #  , customer_constant_16 = customer_constant_16
                                        #  , customer_constant_17 = customer_constant_17
                                        #  , customer_constant_18 = customer_constant_18
                                        #  , customer_constant_19 = customer_constant_19
                                        #  , customer_constant_20 = customer_constant_20
                                        #  , user_defined_1 = user_defined_1
                                        #  , user_defined_2 = user_defined_2
                                        #  , user_defined_3 = user_defined_3
                                        #  , user_defined_4 = user_defined_4
                                        #  , user_defined_5 = user_defined_5
                                        #  , user_defined_6 = user_defined_6
                                        #  , user_defined_7 = user_defined_7
                                        #  , user_defined_8 = user_defined_8
                                        #  , user_defined_9 = user_defined_9
                                        #  , user_defined_10 = user_defined_10
                                        #  , user_defined_11 = user_defined_11
                                        #  , user_defined_12 = user_defined_12
                                        #  , user_defined_13 = user_defined_13
                                        #  , user_defined_14 = user_defined_14
                                        #  , user_defined_15 = user_defined_15
                                        #  , user_defined_16 = user_defined_16
                                        #  , user_defined_17 = user_defined_17
                                        #  , user_defined_18 = user_defined_18
                                        #  , user_defined_19 = user_defined_19
                                        #  , user_defined_20 = user_defined_20
                                        , customer_customer_w_tax = customer_customer_w_tax
                                        , customer_limit_number_of_dealer_logins_to = customer_limit_number_of_dealer_logins_to
                                        , customer_days_to_hold_quotes = customer_days_to_hold_quotes
                                        #  , customer_enable_price_calculation = customer_enable_price_calculation
                                        #  , customer_enable_freight_calculation = customer_enable_freight_calculation
                                        #  , customer_collection_display = customer_collection_display
                                        #  , customer_internal_xml_id = customer_internal_xml_id
                                        #  , customer_client_quote_letter_verbiage = customer_client_quote_letter_verbiage
                                        #  , customer_booked_orders = customer_booked_orders
                                        #  , customer_deposits = customer_deposits
                                        #  , customer_balance_due = customer_balance_due
                                        #  , customer_open_ar = customer_open_ar
                                        #  , customer_30_day_ar = customer_30_day_ar
                                        #  , customer_60_day_ar = customer_60_day_ar
                                        #  , customer_90_day_ar = customer_90_day_ar
                                        #  , customer_120_day_ar = customer_120_day_ar
                                        #  , customer_unapplied = customer_unapplied
                                        #  , customer_total_open_ar = customer_total_open_ar
                                        #  , customer_ytd = customer_ytd
                                        #  , customer_previous_year = customer_previous_year
                                        #  , customer_high_sale = customer_high_sale
                                        #  , customer_py_high_sale = customer_py_high_sale
                                        #  , customer_cogs = customer_cogs
                                        #  , customer_py_cogs = customer_py_cogs
                                        , customer_avg_days_to_pay = customer_avg_days_to_pay
                                        , customer_pv_avg_days_to_pay = customer_pv_avg_days_to_pay
                                        , customer_times_past_due = customer_times_past_due
                                        , customer_py_times_past_due = customer_py_times_past_due
                                                                    
                                        , row_is_current = row_is_current, row_start_date = row_start_date, row_end_date = row_end_date
                                        , row_change_reason = row_change_reason, import_version = 'v 1.0'
                                        , import_batch = 0
                                        , import_user = 'admin'
                                        )
                dim_customer.save()
                #messages.success(request, 'Form successfully submitted') # Any message you wish
                #print(str(len(dim_customers))+' dim_customer update successful')
            from django.http import HttpResponseRedirect
            #return HttpResponseRedirect("/dim_product_group")

    number_of_records_imported = Dim_customer.objects.count()
    
    last_import_time = Dim_customer.objects.extra(order_by = ['row_end_date'])

    # ---------------------------------------------------------------------------------------------------------------------------------------------
    # Use this block after table is added to dim_table

    # last_import_time = last_import_time[number_of_records_imported-1].row_end_date
    # table = Dim_table.objects.filter(table_name='jcwf_dim_product_group')
    # tablename = Dim_table.objects.get(table_name='jcwf_dim_product_group').table_name
    # table.update(number_of_records_imported=number_of_records_imported, row_end_date=last_import_time
    #            , row_change_reason = 'normal update')

    # last_import_time = Dim_table.objects.get(table_name='jcwf_dim_product_group').row_end_date 
    # total_records = Dim_table.objects.get(table_name='jcwf_dim_product_group').number_of_records_imported 

    # ---------------------------------------------------------------------------------------------------------------------------------------------
    # Use this block before table is added to dim_table

    tablename = 'test'
    last_import_time = '8/3/2021'
    total_records = 'test'

    # ---------------------------------------------------------------------------------------------------------------------------------------------
    #dim_customer_df = pd.DataFrame(list(Dim_product.objects.all().values()))
    dim_customers_df = Dim_customer.objects.all()
    dim_customers_df = read_frame(dim_customers_df)
    customer_names = dim_customers_df['customer_name'].values.tolist()
    customer_ids = dim_customers_df['customer_account'].values.tolist()
    
    context = {'tablename':tablename, 'last_import_time':last_import_time
             , 'total_records':total_records, 'customer_names':customer_names, 'customer_ids':customer_ids}
             
    
    #print(datetime.now() - app_start_time)
    from django.http import HttpResponseRedirect
    #return HttpResponseRedirect("/dim_customer_group")
    return render(request, 'dim_customer_input.html', context)

@login_required(login_url="/accounts/login/")
def employee_(request, id):
    return redirect('/employee/list')

