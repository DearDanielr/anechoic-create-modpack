execute in minecraft:overworld as @e[type=illagerinvasion:invoker,tag=!anechoic_balanced_invoker] run function anechoic_balance:balance_invoker
execute in minecraft:the_nether as @e[type=illagerinvasion:invoker,tag=!anechoic_balanced_invoker] run function anechoic_balance:balance_invoker
execute in minecraft:the_end as @e[type=illagerinvasion:invoker,tag=!anechoic_balanced_invoker] run function anechoic_balance:balance_invoker
schedule function anechoic_balance:scan_invokers 1s replace
