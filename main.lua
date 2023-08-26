local players = game:GetService("Players")
local httpservice = game:GetService("HttpService")

if game:GetService("TextChatService").ChatVersion ~= Enum.ChatVersion.LegacyChatService then
	local events = game:GetService("ReplicatedStorage"):WaitForChild("DefaultChatSystemChatEvents")
	local messageDoneFiltering = events:WaitForChild("OnMessageDoneFiltering")
	
	messageDoneFiltering.OnClientEvent:Connect(function(message)
	  local player = players:FindFirstChild(message.FromSpeaker)
	  local message = message.Message or ""

	  if player then
		print(player.Name .. ": " .. message)
		local response = request({
			Url = "http://localhost:9800",
			Method = "GET", -- Optional | GET, POST, HEAD, etc
			Headers = {["Content-Type"] = "text/plain"}, -- Optional | HTTP Headers
		})
		
		if response.Body == "im on" then
			local mainresponse = request({
				Url = "http://localhost:9800",
				Method = "POST", -- Optional | GET, POST, HEAD, etc
				Headers = {["Content-Type"] = "text/plain"}, -- Optional | HTTP Headers
				Body = message.."\n"..player.Name
			})
			
			if mainresponse.Success then
				print(mainresponse.Body)
			end
		end
	  end
	end)
else
	players.PlayerChatted:Connect(function(chattype, player, message)
		if player then
			print(player.Name .. ": " .. message)
			local response = request({
				Url = "http://localhost:9800",
				Method = "GET", -- Optional | GET, POST, HEAD, etc
				Headers = {["Content-Type"] = "text/plain"}, -- Optional | HTTP Headers
			})
			
			if response.Body == "im on" then
				local mainresponse = request({
					Url = "http://localhost:9800",
					Method = "POST", -- Optional | GET, POST, HEAD, etc
					Headers = {["Content-Type"] = "text/plain"}, -- Optional | HTTP Headers
					Body = message.."\n"..player.Name
				})
				
				if mainresponse.Success then
					print(mainresponse.Body)
				end
			end
		end
	end)
end
