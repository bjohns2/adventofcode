test_input = "broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output"

easy_test_input = "broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"

my_input = "%jf -> cr, dn
%fd -> hm, jx
%mb -> bq, cr
&mr -> qt
%qd -> cr, dg
%rs -> hh
%xl -> gq, vj
%zl -> qn
%tj -> cr, qd
%fn -> hn
%qc -> tf
%fh -> jj, vj
&kk -> qt
%qn -> jx, fn
%hm -> jx, fq
%cm -> vj, fh
%jj -> vj, lp
%dr -> vj, qc
broadcaster -> db, hd, cm, xf
%fq -> jx, zk
%hd -> jx, zl
&qt -> rx
&vj -> bb, qc, cm
%tt -> bd
%sf -> jx
%rg -> nl, hr
%zk -> jx, sf
%lp -> cz, vj
%xf -> mb, cr
&cr -> dg, bq, kk, xf, gm
%nb -> vj, dr
%dg -> vm
%ql -> nl
&gl -> qt
&nl -> db, hr, mr, hh, hk, rs, bn
%ff -> ql, nl
%rb -> cr
%lc -> vj
%vm -> gm, cr
%tf -> vj, xl
%hr -> kf
%kf -> xx, nl
&bb -> qt
%ml -> nl, bn
%bq -> tj
%db -> ml, nl
%hn -> jx, tt
%dn -> cr, rb
%gm -> qs
%gq -> lc, vj
%hh -> rg
%bd -> fd
%xx -> nl, ff
%qs -> jf, cr
&jx -> fn, bd, tt, gl, zl, hd
%cz -> nb, vj
%bn -> hk
%hk -> rs
"

class Pulse
  attr_accessor :from_node
  attr_accessor :destination_node
  attr_accessor :power

  def initialize(from_node, destination_node, power)
    @from_node = from_node
    @destination_node = destination_node
    @power = power
  end

  def to_s
    "#{power} pulse #{from_node} -> #{destination_node}"
  end
end

class Output
  attr_accessor :name
  attr_accessor :destination_nodes

  def initialize(name)
    @name = name
    @destination_nodes = []
  end

  def to_s
    "output"
  end

  def handle_pulse(pulse)
    puts "low pulse to RX!" if pulse.power == 'low' && name == 'rx'
    []
  end
end

class FlipFlop
  attr_accessor :name
  attr_accessor :destination_nodes
  attr_accessor :state

  def initialize(name, destination_nodes)
    @name = name
    @destination_nodes = destination_nodes
    @state = 'off'
  end

  def to_s
    "Flip-flop #{@name} currently #{@state}, destinations [#{@destination_nodes.join(',')}]"
  end
  
  def handle_pulse(pulse)
    # puts "handling pulse to flip flop #{name}"
    if pulse.power == 'low'
      if @state == 'off'
        @state = 'on'
        return @destination_nodes.map do |destination_node|
          Pulse.new(name, destination_node.name, 'high')
        end
      else
        @state = 'off'
        return @destination_nodes.map do |destination_node|
          Pulse.new(name, destination_node.name, 'low')
        end
      end
    end
    []
  end
end

class Conjunction
  attr_accessor :name
  attr_accessor :destination_nodes
  attr_accessor :last_pulses_from_inputs

  def initialize(name, destination_nodes)
    @name = name
    @destination_nodes = destination_nodes
    @last_pulses_from_inputs = {}
  end

  def to_s
    "Conjunction #{@name}, last pulses #{last_pulses_from_inputs}, destinations [#{@destination_nodes.join(',')}]"
  end  

  def handle_pulse(pulse)
    last_pulses_from_inputs[pulse.from_node] = pulse.power
    if last_pulses_from_inputs.all?{|input, pulse_power| pulse_power == 'high'}
      return @destination_nodes.map{ |destination_node| Pulse.new(name, destination_node.name, 'low')}
    else
      # puts @destination_nodes.join(',')
      return @destination_nodes.map{ |destination_node| Pulse.new(name, destination_node.name, 'high')}
    end
  end
end

class Broadcaster
  attr_accessor :name
  attr_accessor :destination_nodes

  def initialize(destination_nodes)
    @name = 'broadcaster'
    @destination_nodes = destination_nodes
  end

  def to_s
    "Broadcaster , destinations [#{@destination_nodes.join(',')}]"
  end  

  def handle_pulse(pulse)
    @destination_nodes.map do |destination_node|
      Pulse.new(name, destination_node.name, pulse.power)
    end
  end
end

def parse_input(input)
  lines = input.split("\n")
  nodes = []
  # all_destination_node_names = []
  lines.each do |line|
    start = line.split(' -> ')[0]
    destination_nodes = line.split(' -> ')[1].split(', ')
    if start == 'broadcaster'
      nodes << Broadcaster.new(destination_nodes)
    elsif start[0] == '%'
      node = start[1..-1]
      nodes << FlipFlop.new(node, destination_nodes)
    elsif start[0] == '&'
      node = start[1..-1]
      nodes << Conjunction.new(node, destination_nodes)
    end
    # all_destination_node_names += destination_nodes
  end
  # all_destination_node_names.uniq.each do |dn|
  #   if 
  # end
  output_nodes = []
  nodes.each do |node|
    node.destination_nodes.map do |dn| 
      if nodes.find{|n| n.name == dn} == nil
        output_nodes << Output.new(dn)
      end
    end
  end
  nodes += output_nodes
  nodes.each do |node|
    node.destination_nodes = node.destination_nodes.map{|dn| nodes.find{|n| n.name == dn}}
    node.destination_nodes.each do |destination_node|
      if destination_node.class == Conjunction
        destination_node.last_pulses_from_inputs[node.name] = 'low'
      end
    end
  end
end

def solution(input)
  nodes = parse_input(input)
  # nodes.map{|n| puts n}
  puts "========================="
  total_low_pulses = 0
  total_high_pulses = 0
  total_button_presses = 0
  (0...5000000000000000).each do |i|
    puts i if i%1000000 == 0
    pulses_to_handle = [Pulse.new(nil, 'broadcaster', 'low')]
    total_button_presses += 1
    while pulses_to_handle.size > 0
      pulse_to_handle = pulses_to_handle.shift
      total_low_pulses += 1 if pulse_to_handle.power == 'low'
      total_high_pulses += 1 if pulse_to_handle.power == 'high'
      if pulse_to_handle.power == 'low' && pulse_to_handle.destination_node == 'rx'
        puts "GOT IT ON PUSE #{i}" 
        return 'hi'
      end
      destination_node = nodes.find{|n| n.name == pulse_to_handle.destination_node}
      next if destination_node == nil
      new_pulses = destination_node.handle_pulse(pulse_to_handle)
      pulses_to_handle += new_pulses
      # puts "new pulses:"
      # new_pulses.map{|p| puts p}
      # puts "total_low_pulses: #{total_low_pulses}"
      # puts "total_high_pulses: #{total_high_pulses}"
    end
    # puts "total_button_presses: #{total_button_presses}"
    # puts "total_low_pulses: #{total_low_pulses}"
    # puts "total_high_pulses: #{total_high_pulses}"
  end
  puts "total_button_presses: #{total_button_presses}"
  puts "total_low_pulses: #{total_low_pulses}"
  puts "total_high_pulses: #{total_high_pulses}"
  puts "total: #{total_low_pulses * total_high_pulses}"
end

solution(my_input)

# 5000000 is too low
# 50000000 is too low
# 500  is too low