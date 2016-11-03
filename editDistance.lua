
require 'torch'
local editDistance = torch.class("editDistance")

function editDistance:cal_editDistance(target,prediction)
  dist = self:_editDistance(target,prediction,#target,#prediction)
  return dist/(#target)
end
  
function editDistance:_editDistance(target,prediction,len_tar,len_pred)
  if len_tar < 1 then
    return len_pred
  elseif len_pred < 1 then 
    return len_tar
  elseif string.sub(target,len_tar,len_tar)==string.sub(prediction,len_pred,len_pred) then
    return self:_editDistance(target,prediction,len_tar-1,len_pred-1)
  else
    local substitution = self:_editDistance(target,prediction,len_tar-1,len_pred-1)
    local insertion = self:_editDistance(target,prediction,len_tar-1,len_pred)
    local deletion = self:_editDistance(target,prediction,len_tar,len_pred-1)
    return (1 + math.min(substitution, insertion, deletion))
  end
end
  
  
  
  function editDistance:sequenceErrorRate(target, prediction)
    local d = torch.Tensor(#target + 1, #prediction + 1):zero()
    for i = 1, #target + 1 do
        for j = 1, #prediction + 1 do
            if (i == 1) then
                d[1][j] = j - 1
            elseif (j == 1) then
                d[i][1] = i - 1
            end
        end
    end

    for i = 2, #target + 1 do
        for j = 2, #prediction + 1 do
            if (target[i - 1] == prediction[j - 1]) then
                d[i][j] = d[i - 1][j - 1]
            else
                local substitution = d[i - 1][j - 1] + 1
                local insertion = d[i][j - 1] + 1
                local deletion = d[i - 1][j] + 1
                d[i][j] = torch.min(torch.Tensor({ substitution, insertion, deletion }))
            end
        end
    end
    local errorRate = d[#target + 1][#prediction + 1] / #target
    return errorRate
end
  

--[[
local tar = {'l','i','t','h','e'}
local  pred = {'W','O','U','L','D'}
  
local d1 = editDistance:sequenceErrorRate(tar, pred)
local d2 = editDistance:cal_editDistance(tar,pred)
print (d1,d2) --]]
  