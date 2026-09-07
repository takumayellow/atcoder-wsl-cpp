input = gets.chomp
count = 0
for i in 0...input.length do
  if input[i]=="1"
    count += 1
  end
end
puts count
