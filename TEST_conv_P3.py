import csv, os, codecs
# import pdb if debugging
#, pdb


# read in csv file from transamerica
openfile = open('transactions.csv')

# while file is open write to it in memory
with open('temp1.csv', 'w', newline='') as outputfile:
	# create reader and writer objects
	reader1 = csv.reader(openfile)
	writer1 = csv.writer(outputfile)
	# iterate through file appending investment action at end of reach row
	for row in reader1:
		if 'Contribution' == row[0]:
			row.append(str('Buy'))
			writer1.writerow(row)
			
		elif 'Plan Service Credit' == row[0]:
			row.append(str('Buy')) 
			writer1.writerow(row)
			
		elif 'Transfer Into Fund' == row[0]:
			row.append(str('Buy'))
			writer1.writerow(row)
			
		elif 'Daily Dividends' == row[0]:
			row.append(str('ReinvDiv')) 
			writer1.writerow(row)
			
		elif 'Periodic Dividends' == row[0]:
			row.append(str('ReinvDiv')) 		
			writer1.writerow(row)
			
		elif 'Periodic Capital Gains' == row[0]:
			row.append(str('ReinvDiv')) 
			writer1.writerow(row)
			
		elif 'Administrative Fee - Pro-Rata' == row[0]:
			row.append(str('Sell'))
			writer1.writerow(row)
			
		elif 'Transfer Out of Fund' == row[0]:
			row.append(str('Sell'))
			writer1.writerow(row)
			
		else:
			writer1.writerow(row)	
			
openfile.close()

# open temp file1 outputted from previous step
openfile2 = open('temp1.csv')

# while file is open write to it in memory
with open('temp2.csv','w', newline='') as outputfile2:
	
	# create reader object
	reader2 = csv.reader(openfile2)
	# skip first row in new file
	next(reader2,None)
	
	# create writer object
	writer2 = csv.writer(outputfile2)
	
	# create new header row in new file
	writer2.writerow(['Transaction Type','Date','Source','Fund Name','Unit Count','Unit Value','Transaction Amount','Investment Action','Ticker'])
			
	# iterate through file appending ticker symbol at end of reach row and replacing name from transamerica to the name
	# quicken recognizes with .replace(old,new)
	for row in reader2:
		#print(reader2.line_num)
		if 'American Century Equity Income R6' == row[3]:
			row.append(str('AEUDX'))
			row[3] = row[3].replace('American Century Equity Income R6','American Century Equity Income Fund R6 Class')
			writer2.writerow(row)
			
		elif 'American Century Mid Cap Value R6' == row[3]:
			row.append(str('AMDVX'))
			row[3] = row[3].replace('American Century Mid Cap Value R6','American Century Mid Cap Value Fund R6 Class')
			writer2.writerow(row)
			
		elif 'American Funds EuroPacific Gr R5' == row[3]:
			row.append(str('RERFX'))
			row[3] = row[3].replace ('American Funds EuroPacific Gr R5','American Funds EuroPacific Growth Fund® Class R-5')
			writer2.writerow(row)	
			
		elif 'American Funds EuroPacific Gr R6' == row[3]:
			row.append(str('RERGX'))
			row[3] = row[3].replace('American Funds EuroPacific Gr R6','American Funds EuroPacific Growth Fund Class R-6')
			writer2.writerow(row)
			
		elif 'American Funds EuroPacific Growth R5E' == row[3]:
			row.append(str('RERHX'))
			row[3].replace('American Funds EuroPacific Growth R5E','American Funds EuroPacific Growth Fund® Class R-5E')
			writer2.writerow(row)
			
		elif 'American Funds Inflation Linked Bond R-6' == row[3]:
			row.append(str('RILFX'))
			row[3] = row[3].replace('American Funds Inflation Linked Bond R-6','American Funds Inflation Linked Bond Fund Class R-6')
			writer2.writerow(row)
			
		elif 'AMG Managers Fairpointe Mid Cap I' == row[3]:
			row.append(str('ABMIX'))
			row[3] = row[3].replace('AMG Managers Fairpointe Mid Cap I','AMG Managers Fairpointe Mid Cap Fund Class I')
			writer2.writerow(row)
			
		elif 'AQR Large Cap Defensive Style R6' == row[3]:
			row.append(str('QUERX'))
			row[3] = row[3].replace('AQR Large Cap Defensive Style R6','AQR Large Cap Defensive Style Fund Class R6')
			writer2.writerow(row)
			
		elif 'BlackRock High Yield Bond K' == row [3]:
			row.append(str('BRHYX'))
			row[3] = row[3].replace('BlackRock High Yield Bond K', 'BlackRock High Yield Bond Portfolio Class K')
			writer2.writerow(row)
			
		elif 'BlackRock Inflation Protected Bond Instl' == row[3]:
			row.append(str('BPRIX'))
			row[3] = row[3].replace('BlackRock Inflation Protected Bond Instl', 'BlackRock Inflation Protected Bond Fund Institutional Shares')
			writer2.writerow(row)
			
		elif 'ClearBridge Dividend Strat I' == row[3]:
			row.append(str('SOPYX'))
			row[3] = row[3].replace('ClearBridge Dividend Strat I', 'ClearBridge Dividend Strategy Fund Class I')
			writer2.writerow(row)
			
		elif 'Cohen & Steers Instl Realty Shares' == row[3]:
			row.append(str('CSRIX'))
			row[3] = row[3].replace('Cohen & Steers Instl Realty Shares', 'Cohen & Steers Institutional Realty Shares')
			writer2.writerow(row)
			
		elif 'Cohen & Steers Realty Shares' == row[3]:
			row.append(str('CSRSX'))
			row[3] = row[3].replace('Cohen & Steers Realty Shares', 'Cohen & Steers Realty Shares Fund')
			writer2.writerow(row)
			
		elif 'Delaware Emerging Markets Instl' == row[3]:
			row.append(str('DEMIX'))
			row[3] = row[3].replace('Delaware Emerging Markets Instl', 'Delaware Emerging Markets Fund Institutional Class')
			writer2.writerow(row)
			
		elif 'Delaware Emerging Markets R6' == row[3]:
			row.append(str('DEMZX'))
			row[3] = row[3].replace('Delaware Emerging Markets R6','Delaware Emerging Markets Fund Class R6')
			writer2.writerow(row)
			
		elif 'Fidelity Contrafund' == row[3]:
			row.append(str('FCNTX'))
			row[3] = row[3].replace('Fidelity Contrafund', 'Fidelity Contrafund Fund')
			writer2.writerow(row)

		elif 'Fidelity Contrafund K6' == row[3]:
			row.append(str('FLCNX'))
			row[3] = row[3].replace('Fidelity Contrafund K6', 'Fidelity Contrafund K6')
			writer2.writerow(row)
			
		elif 'JHancock International Growth I' == row[3]:
			row.append(str('GOGIX'))
			row[3] = row[3].replace('JHancock International Growth I', 'JHancock International Growth I')
			writer2.writerow(row)
			
		elif 'JHancock International Growth R6' == row[3]:
			row.append(str('JIGTX'))
			row[3] = row[3].replace('JHancock International Growth R6','John Hancock Funds International Growth Fund Class R6')
			writer2.writerow(row)
			
		elif 'Metropolitan West Total Return Bond I' == row[3]:
			row.append(str('MWTIX'))
			row[3] = row[3].replace('Metropolitan West Total Return Bond I','Metropolitan West Total Return Bond I')
			writer2.writerow(row)
			
		elif 'Metropolitan West Total Return Bond Plan' == row[3]:
			row.append(str('MWTSX'))
			row[3] = row[3].replace('Metropolitan West Total Return Bond Plan','Metropolitan West Total Return Bond Fund Plan Class')
			writer2.writerow(row)
			
		elif 'Oakmark Investor' == row[3]:
			row.append(str('OAKMX'))
			row[3] = row[3].replace('Oakmark Investor', 'Oakmark I')
			writer2.writerow(row)
			
		elif 'PIMCO Low Duration Instl' == row[3]:
			row.append(str('PTLDX'))
			row[3] = row[3].replace('PIMCO Low Duration Instl', 'PIMCO Low Duration Instl')
			writer2.writerow(row)
			
		elif 'PIMCO StocksPLUS Small Institutional' == row[3]:
			row.append(str('PSCSX'))
			row[3] = row[3].replace('PIMCO StocksPLUS Small Institutional', 'PIMCO StocksPLUS Small Institutional')
			writer2.writerow(row)
			
		elif 'Standard Stable Asset Fund II' == row[3]:
			row.append(str(''))
			row[3] = row[3].replace('Standard Stable Asset Fund II', 'Standard Stable Asset Fund II')
			writer2.writerow(row)
			
		elif 'Vanguard Institutional Index I' == row[3]:
			row.append(str('VINIX'))
			row[3] = row[3].replace('Vanguard Institutional Index I', 'Vanguard Institutional Index Fund Institutional Shares')
			writer2.writerow(row)
			
		elif 'Vanguard Interm-Term Bond Index Adm' == row[3]:
			row.append(str('VBILX'))
			row[3] = row[3].replace('Vanguard Interm-Term Bond Index Adm', 'Vanguard Intermediate-Term Bond Index Fund Admiral Shares')
			writer2.writerow(row)
			
		elif 'Vanguard Interm-Term Bond Index I' == row[3]:
			row.append(str('VBIMX'))
			row[3] = row[3].replace('Vanguard Interm-Term Bond Index I','Vanguard Intermediate-Term Bond Index Fund Institutional Shares')
			writer2.writerow(row)
			
		elif 'Vanguard Mid Cap Index I' == row[3]:
			row.append(str('VMCIX'))
			row[3] = row[3].replace('Vanguard Mid Cap Index I', 'Vanguard Mid-Cap Index Fund Institutional Shares')
			writer2.writerow(row)
			
		elif 'Vanguard Small Cap Index I' == row[3]:
			row.append(str('VSCIX'))
			row[3] = row[3].replace('Vanguard Small Cap Index I', 'Vanguard Small-Cap Index Fund Institutional Shares')
			writer2.writerow(row)
			
		elif 'Vanguard Total Intl Stock Index Admiral' == row[3]:
			row.append(str('VTIAX'))
			row[3] = row[3].replace('Vanguard Total Intl Stock Index Admiral', 'Vanguard Total International Stock Index Fund Admiral Shares')
			writer2.writerow(row)	
					
		else:
			writer2.writerow(row)
		
# close file
openfile2.close()

openfile3 = open('temp2.csv')

# while file is open write to it in memory
with open('transactions_final.csv','w', newline='') as outputfile3:
	
	reader3 = csv.reader(openfile3)
	
	# skip first (header) row in file
	next(reader3,None)

    # add header
	writer3 = csv.writer(outputfile3)
	writer3.writerow(['Transaction Type','Date','Source','Fund Name','Unit Count','Unit Value','Transaction Amount','Investment Action','Ticker'])
				
	# iterate through file stripping excess spaces
	for row in reader3:
		#row = [x.rstrip() for x in row]
		if row[2][-1] == ' ':
			row[2] = row[2].rstrip()
			writer3.writerow(row)
		
#close file	
openfile3.close()

#clean up temp files
os.remove("./temp1.csv")
os.remove("./temp2.csv")

