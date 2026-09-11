attribute @s minecraft:generic.max_health modifier add anechoic_balance:invoker_health 0.5 add_multiplied_total
execute store result entity @s Health float 0.0015 run data get entity @s Health 1000
tag @s add anechoic_balanced_invoker
