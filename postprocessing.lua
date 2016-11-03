require 'io'
require 'SequenceError'
require 'editDistance'
local postprocessing = torch.class('postprocessing')


function postprocessing:__init()
  end
file_read = io.open('/home/sbp3624/CTCSpeechRecognition/python_scripts/lexicon.txt','r')
io.input(file_read)
local lines =  {}
counter = 0
local max_words = 100
for line in io.lines() do
  f_line, val = string.gsub(line,'[%d%s]','')
  f_line = string.upper(f_line)
  if counter < max_words then 
    table.insert(lines,f_line)
    counter = counter + 1
  else
    break
  end
 end
--print (lines)
--print (count)

function postprocessing:cal_CER(predict)
  local curr_CER = 0
  local prev_CER = 0
  local predict_word=predict
  for key,target in pairs (lines) do
    if key == 1 then
      prev_CER = SequenceError:calculateCER(target, predict) 
      if prev_CER < 0.75 then
        predict_word = target
      end
    else
      curr_CER = SequenceError:calculateCER(target, predict)
      if curr_CER < prev_CER and curr_CER<0.75 then
        prev_CER = curr_CER
        predict_word = target
      end
    end
  end

  return predict_word
 end       
  
  
  
  

