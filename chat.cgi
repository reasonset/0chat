#!/usr/bin/env ruby

require 'erb'
require 'cgi'

CHAT_HTML = File.read("template.erb")

def esc(str)
  str && str.gsub("&", "&amp;").gsub("<", "&lt;").gsub(">", "&gt;").gsub('"', "&quot;")
end

File.open("sessionlock.lck", "w") do |f|
  f.flock(File::LOCK_EX)
  chat = nil
  begin
    begin
      chat = Marshal.load File.open("chat.log")
    rescue 
      chat = []
    end
    cgi = CGI.new
    now = Time.now
    break if !cgi["name"] || cgi["name"].empty? || !cgi["chat"] || cgi["chat"].empty?
    chat.unshift({name: esc(cgi["name"]), timestamp: now.strftime("%y-%m-%d %T"), chat: esc(cgi["chat"])&.[](0, 1024)})
    chat = chat[0,30]
    if chat.length > 500
      require 'json'
      File.open(now.strftime('archives/chat-%y%m%d%H%M%S.json'), "w") {|f| JSON.dump(chat, f) }
      chat = chat[0, 30]
    end
    File.open("chat.log", "w") {|f| Marshal.dump chat, f }
    File.open("chat.html", "w") {|f| f.puts ERB.new(CHAT_HTML).result(binding)}
  ensure
    f.flock(File::LOCK_UN)
  end
end

puts "Status: 204"
puts