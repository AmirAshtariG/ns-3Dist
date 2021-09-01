/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/*
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation;
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */

#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/internet-module.h"
#include "ns3/point-to-point-module.h"
#include "ns3/applications-module.h"
#include "ns3/random-variable-stream.h"
#include "ns3/log.h"
#include <iostream>
#include <fstream>

// Default Network Topology
//
//       10.1.1.0
// n0 -------------- n1
//    point-to-point
//
 
using namespace ns3;

NS_LOG_COMPONENT_DEFINE ("ExtremeExample");

int
main (int argc, char *argv[])
{

  LogComponentEnableAll (LOG_PREFIX_TIME);
  LogComponentEnableAll (LOG_PREFIX_FUNC);
  LogComponentEnableAll (LOG_PREFIX_NODE);
  LogComponentEnable("ExtremeExample", LOG_LEVEL_ALL);
  CommandLine cmd (__FILE__);
  cmd.Parse (argc, argv);

  RngSeedManager seed;
  

  double loc =1;
  double scale = 0.5;
  Ptr<ExtremeRandomVariable> x = CreateObject<ExtremeRandomVariable> ();
  x->SetAttribute ("loc", DoubleValue (loc));
  x->SetAttribute ("scale", DoubleValue (scale));

  std::ofstream myfile;
  myfile.open("RandExtreme2.txt");


 // NS_LOG_INFO("The val of rand is:" <<x->GetValue());
  for (int j=0; j<8; j++)
  {
  seed.SetSeed (j);
  for (int i =0; i<100000; i++)
  {
    myfile << x->GetValue() << "\n";
  }
  }
  myfile.close();


  Simulator::Run ();
  Simulator::Destroy ();
  return 0;
}
