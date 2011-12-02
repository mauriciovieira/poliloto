require "lib.show"
local html = require "lib.html"

-----------------------------------------------------------
--- testing table.show

t = {1, {2, 3, 4}, default = {"a", "b", d = {12, "w"}, e = 14}}
t.g = t.default

print("-----------------------------------")
print(table.show(t))                -- shows __unnamed__ table

tt = {1, h = {["p-q"] = "a", b = "e", c = {color = 3, name = "abc"}}, 2}

f = table.show
tt[f] = "OK"

print("-----------------------------------")
print(table.show(tt, "tt", "--oo-- ")) -- shows some initial 'indent'

t.m = {}
t.g.a = {}
t.g.a.c = t
t.tt = tt.new
t.show = table.show

print("-----------------------------------")
print(table.show(t, "t"))            -- most typical use

print("-----------------------------------")
print(table.show(math.tan, "tan"))   -- not a table is OK

print("-----------------------------------")
s = "a string"
print(table.show(s, "s"))            -- not a table is OK

print(table.show(html,"html"))
io.input('../resultados/D_MEGA.HTM')
local h = io.read("*all")
local parsed = html.collect(h)
io.close()
print(table.show(parsed))

